from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import ActionItem, Cluster, Decision, FeedbackCycle, FeedbackItem, Membership, Project, Vote
from .services import ensure_default_clusters, process_transcript


class RetroLoopTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alex", password="secret", first_name="Alex")
        self.other = User.objects.create_user(username="sam", password="secret", first_name="Sam")
        self.project = Project.objects.create(name="Data Platform", facilitator=self.user)
        Membership.objects.create(project=self.project, user=self.user, role=Membership.Role.FACILITATOR)
        Membership.objects.create(project=self.project, user=self.other, role=Membership.Role.MEMBER)
        self.cycle = FeedbackCycle.objects.create(project=self.project, title="Week 1")

    def test_register_creates_user_without_email(self):
        response = self.client.post(
            reverse("register"),
            {"username": "newuser", "display_name": "New User", "password": "secret123"},
        )

        self.assertRedirects(response, reverse("project-list"))
        user = User.objects.get(username="newuser")
        self.assertEqual(user.first_name, "New User")
        self.assertEqual(user.email, "")

    def test_project_page_exists(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse("project-detail", args=[self.project.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Data Platform")

    def test_user_sees_only_own_feedback_before_reveal(self):
        FeedbackItem.objects.create(cycle=self.cycle, author=self.user, category=FeedbackItem.Category.START, body="Start demos")
        FeedbackItem.objects.create(cycle=self.cycle, author=self.other, category=FeedbackItem.Category.STOP, body="Stop scope creep")
        self.client.force_login(self.user)

        response = self.client.get(reverse("cycle-detail", args=[self.cycle.pk]))

        self.assertContains(response, "Start demos")
        self.assertNotContains(response, "Stop scope creep")

    def test_anonymous_feedback_hides_author_after_reveal(self):
        FeedbackItem.objects.create(
            cycle=self.cycle,
            author=self.other,
            category=FeedbackItem.Category.CONTINUE,
            body="Continue weekly planning",
            is_anonymous=True,
        )
        self.cycle.is_revealed = True
        self.cycle.save(update_fields=["is_revealed"])
        self.client.force_login(self.user)

        response = self.client.get(reverse("cycle-detail", args=[self.cycle.pk]))

        self.assertContains(response, "Continue weekly planning")
        self.assertContains(response, "Anonymous")
        self.assertNotContains(response, "Sam")

    def test_reveal_creates_default_clusters(self):
        FeedbackItem.objects.create(cycle=self.cycle, author=self.user, category=FeedbackItem.Category.START, body="Start writing notes")
        self.client.force_login(self.user)

        response = self.client.post(reverse("reveal-feedback", args=[self.cycle.pk]))

        self.assertRedirects(response, reverse("board", args=[self.cycle.pk]))
        self.cycle.refresh_from_db()
        self.assertTrue(self.cycle.is_revealed)
        self.assertEqual(self.cycle.clusters.count(), 3)
        self.assertEqual(self.cycle.feedback_items.get().cluster.title, "Start")

    def test_cluster_title_can_be_edited(self):
        cluster = Cluster.objects.create(cycle=self.cycle, title="Start")
        self.client.force_login(self.user)

        response = self.client.post(reverse("cluster-rename", args=[cluster.pk]), {"title": "Start doing"})

        self.assertRedirects(response, reverse("board", args=[self.cycle.pk]))
        cluster.refresh_from_db()
        self.assertEqual(cluster.title, "Start doing")

    def test_user_can_cast_three_votes_with_multiple_votes_on_same_cluster(self):
        cluster = Cluster.objects.create(cycle=self.cycle, title="Start")
        self.client.force_login(self.user)

        for _ in range(4):
            self.client.post(reverse("vote", args=[cluster.pk]))

        vote = Vote.objects.get(cluster=cluster, voter=self.user)
        self.assertEqual(vote.count, 3)

    def test_voting_results_show_after_close(self):
        cluster = Cluster.objects.create(cycle=self.cycle, title="Start")
        Vote.objects.create(cycle=self.cycle, cluster=cluster, voter=self.user, count=2)
        self.cycle.is_revealed = True
        self.cycle.save(update_fields=["is_revealed"])
        self.client.force_login(self.user)

        self.client.post(reverse("close-voting", args=[self.cycle.pk]))
        response = self.client.get(reverse("board", args=[self.cycle.pk]))

        self.cycle.refresh_from_db()
        self.assertTrue(self.cycle.voting_closed)
        self.assertContains(response, "Votes: 2")

    def test_summary_records_decision_and_action_item(self):
        self.client.force_login(self.user)

        self.client.post(reverse("summary", args=[self.cycle.pk]), {"decision-text": "Ship the MVP", "decision": "1"})
        self.client.post(
            reverse("summary", args=[self.cycle.pk]),
            {"action-description": "Create rollout checklist", "action-owner": "Alex", "action-due_date": "", "action": "1"},
        )

        self.assertTrue(Decision.objects.filter(cycle=self.cycle, text="Ship the MVP").exists())
        self.assertTrue(ActionItem.objects.filter(cycle=self.cycle, owner="Alex").exists())

    def test_transcript_processing_extracts_candidates(self):
        result = process_transcript(
            self.cycle,
            "Decision: Use Django for the MVP\nAction: Alex will write tests",
        )

        self.assertIn("Decision: Use Django for the MVP", result.extracted_notes)
        self.assertTrue(Decision.objects.filter(cycle=self.cycle).exists())
        self.assertTrue(ActionItem.objects.filter(cycle=self.cycle, owner="Unassigned").exists())

    def test_default_cluster_service_assigns_feedback_by_category(self):
        item = FeedbackItem.objects.create(
            cycle=self.cycle,
            author=self.user,
            category=FeedbackItem.Category.STOP,
            body="Stop skipping QA",
        )

        ensure_default_clusters(self.cycle)

        item.refresh_from_db()
        self.assertEqual(item.cluster.title, "Stop")
