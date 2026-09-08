from django.test import TestCase
from django.urls import reverse

from .models import Chore, HouseholdMember


class ChoreModelTests(TestCase):
    def test_mark_complete_sets_status_and_timestamp(self):
        chore = Chore.objects.create(title="Take out trash")

        chore.mark_complete()

        chore.refresh_from_db()
        self.assertEqual(chore.status, Chore.Status.COMPLETE)
        self.assertIsNotNone(chore.completed_at)


class ChoreViewTests(TestCase):
    def test_dashboard_lists_pending_chores(self):
        Chore.objects.create(title="Vacuum")

        response = self.client.get(reverse("chore-list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Vacuum")

    def test_create_household_member(self):
        response = self.client.post(reverse("member-create"), {"name": "Alex"})

        self.assertRedirects(response, reverse("chore-list"))
        self.assertTrue(HouseholdMember.objects.filter(name="Alex").exists())

    def test_create_chore_with_assignee(self):
        member = HouseholdMember.objects.create(name="Sam")

        response = self.client.post(
            reverse("chore-create"),
            {
                "title": "Clean kitchen",
                "description": "Wipe counters and sweep floor",
                "assignee": member.pk,
                "due_date": "2026-09-08",
            },
        )

        self.assertRedirects(response, reverse("chore-list"))
        chore = Chore.objects.get(title="Clean kitchen")
        self.assertEqual(chore.assignee, member)
        self.assertEqual(chore.status, Chore.Status.PENDING)

    def test_complete_chore_moves_it_to_completed_view(self):
        chore = Chore.objects.create(title="Do laundry")

        response = self.client.post(reverse("chore-complete", args=[chore.pk]))

        self.assertRedirects(response, reverse("chore-list"))
        chore.refresh_from_db()
        self.assertEqual(chore.status, Chore.Status.COMPLETE)

        dashboard = self.client.get(reverse("chore-list"))
        completed = self.client.get(reverse("completed-chores"))
        self.assertNotContains(dashboard, "Do laundry")
        self.assertContains(completed, "Do laundry")

    def test_edit_chore(self):
        chore = Chore.objects.create(title="Old title")

        response = self.client.post(
            reverse("chore-edit", args=[chore.pk]),
            {
                "title": "New title",
                "description": "",
                "assignee": "",
                "due_date": "",
            },
        )

        self.assertRedirects(response, reverse("chore-list"))
        chore.refresh_from_db()
        self.assertEqual(chore.title, "New title")
