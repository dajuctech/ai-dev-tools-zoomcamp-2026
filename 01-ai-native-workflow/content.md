https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/01-ai-native-workflow

ai-dev-tools-zoomcamp
/01-ai-native-workflow/
alexeygrigorev
alexeygrigorev
Add module summaries and article links
6531bc3
 · 
2 weeks ago
ai-dev-tools-zoomcamp
/01-ai-native-workflow/
Name	Last commit message	Last commit date
..
weekly-feedback
Update module 1 from workshop recording
last month
README.md
Add module summaries and article links
2 weeks ago
README.md
Module 1 — AI-Native Developer Workflow

Tools change every month, but we keep working in much the same way. In this module, we take a vague product idea through specification and context. Then we implement it and run independent QA.

You learn:

Spec-driven development
Context engineering
The product manager, software engineer, and QA roles
Loop engineering
Graph engineering
Recording: AI-Native Developer Workflow

Module summary: The companion article shows how to turn a vague idea into a useful specification, give an agent durable context, break the work into a backlog, and use separate product manager, software engineer, and QA roles to implement and verify the result. It uses a weekly-feedback project to explain spec-driven, loop, and graph engineering.

Read the article: AI-Native Development: Specifications, Loop and Graph Engineering

Example projects

We build the weekly-feedback idea twice to show why we need a specification:

weekly-feedback is the working CLI that Claude Code produces from one vague sentence, with its source and tests included here.
retroloop is the Django retrospective app produced after we specified the product and worked through a groomed GitHub backlog.
Homework

Complete the module with this project:

2026 homework - Build a Django TODO app with the AI tool of your choice. You don't need to know Django.
Previous cohort materials

In 2025, we gave a fuller tour of the tool landscape. Those tools have changed, but we can still use the categories to understand what each kind of tool does.

2025 archived Module 1
Community notes

Add links to your notes above this line.


How to Work with AI Coding Agents: Spec-Driven Development, Context and Loop Engineering, Workflows[
    https://www.youtube.com/watch?v=VUJxJGpaDEs
]

7,310 views  Streamed live on 22 Jul 2026
 Coding agents can now write code faster than we can read it. This workshop covers how to keep control of the development process by specifying the work, preparing project context, and checking the result.

Alexey Grigorev covers four parts of an AI-native development workflow:

Spec-driven development: write down what you want before asking an agent to implement it
Context engineering: give the agent the commands, rules, and project documents it needs
Loop engineering: run agents on small tasks, with checks between runs
Graph engineering: split the work between product manager, engineer, and tester agents

You will also see how to move from a project specification to a backlog, keep reusable instructions in AGENTS.md, define acceptance criteria, test generated code, inspect changes, and review the result before committing it.

Read the written workshop notes: https://alexeyondata.substack.com/p/a...

This workshop is part of AI Dev Tools Zoomcamp, our free course on using AI developer tools to build, test, deploy, extend, and audit software without losing engineering discipline.

Join the free AI Dev Tools Zoomcamp 2026 cohort. The course starts on August 31: https://courses.datatalks.club/regist...

TIMECODES:
00:00 AI DevTools Zoomcamp Overview
08:10 Brainstorming Application Ideas with ChatGPT
13:22 Running Coding Agents Safely in Tmux
17:45 Creating a Feature Specification Before Code
24:37 Defining Retrospective Features and Voting Rules
31:49 Reviewing Outdated One-Shot Code Implementations
37:08 Evaluating Technology Stacks and Framework Trade-offs
42:48 Choosing Django and Defining MVP Constraints
48:03 Generating a Structured Task Backlog
55:42 Repository Creation and Pushing Tasks to GitHub
1:00:08 Bootstrapping the Project Workspace
1:03:07 Context Engineering with AGENTS.md
1:09:46 Defining Process Guidelines and Workflow Rules
1:14:48 Task Grooming via Product Manager Persona
1:21:45 Defining Checkable Acceptance Criteria
1:27:40 Loop Engineering: Automated Multi-Task Goals
1:32:50 Creating the Software Engineer Persona
1:36:00 Quality Assurance and Graph Engineering Workflows
1:41:45 Orchestrator Sub-Agent Execution and Wrap-Up

Connect with DataTalks.Club:
Join the community - https://datatalks.club/slack.html
Subscribe to our Google calendar to have all our events in your calendar - https://calendar.google.com/calendar/...
Check other upcoming events - https://lu.ma/dtc-events
GitHub: https://github.com/DataTalksClub
LinkedIn -   / datatalks-club   
Twitter -   / datatalksclub   
Website - https://datatalks.club/ 

Connect with Alexey
Twitter -   / al_grigor   
Linkedin -   / agrigorev   

Check our free online courses:
ML Engineering course - http://mlzoomcamp.com
Data Engineering course - https://github.com/DataTalksClub/data...
MLOps course - https://github.com/DataTalksClub/mlop... 
LLM course - https://github.com/DataTalksClub/llm-... 
Open-source LLM course: https://github.com/DataTalksClub/open...
AI Dev Tools course: https://github.com/DataTalksClub/ai-d...

👉🏼 Read about all our courses in one place - https://datatalks.club/blog/guide-to-... 

👋🏼 Support/inquiries
If you want to support our community, use this link - https://github.com/sponsors/alexeygri... 

If you’re a company, reach us at alexey@datatalks.club
How this was made
Auto-dubbed
Audio tracks for some languages were automatically generated. Learn more

AI DevTools Zoomcamp Overview
0:00
Hi everyone, welcome to this event. Uh today on the workshop, um I think I have
0:06
a typo here. I need to correct it. So today on the workshop, we are going to talk about um um a few things. So I
0:14
prepared a document. So I linked this document in the here in the description.
0:19
So this is the document we are going to follow. Yes. Go to site. So uh this year
0:24
I'm experimenting with uh releasing the course content as articles. So this is
0:30
the article we're going to follow today. Um so please subscribe to um to my
0:35
substack and I'll be posting more content uh from this course. So this is
0:41
a course that is called AI dev tools zoom camp. So there's also a link there to the course itself.
0:48
So in this course we are going to learn about how using AI for making developers
0:55
more productive. So today we are going to record we're going to have the first
1:00
workshop in the series. In this workshop it's called overview but I want to call it AI native development. So here I'm
1:08
going to uh implement a tool end to end and I'm going to touch things um like um
1:15
what is uh specdriven development, specificationdriven development, what is context engineering, what is loop engineering, what is graph engineering.
1:21
So the last two I added because uh if you're on Twitter, you probably saw uh people talk about these things. So I
1:29
want to cover these things too and explain what they actually are in this session today. Right? So that's uh
1:35
roughly the plan. We will uh take some idea and we will implement this. Um but
1:41
I want to know a little bit about you. So I want to know what is your
1:46
experience with coding agents if you use one of the agents already. So please
1:52
write it uh here in the live chat and also please write um
1:59
um what we want to implement today because I need your ideas. Uh today we
2:04
will pick one of these ideas and implement following this approach. Of course if you don't have some ideas I
2:10
have a backup idea that I can use but it would be more interesting um if you if I
2:17
use your input right. So if you suggest some ideas and then based on these ideas we actually build this together and uh
2:23
please write this in the live chat and also I want to run a poll. I want to
2:29
know what I should use today. So if I should use uh clo C code or if I should
2:36
use codex I like both and the materials that I prepared today they will work for
2:43
most coding agents but still I'm interested uh in knowing what I should
2:49
use today called code or codex right so these are the two that I actively use so
2:57
please let me know what you think and Um while you're doing this while you are
3:03
replying uh what I want to do is to just briefly talk about the course. So I'll
3:08
also you saw the link right? So this is um uh this substack article. It links to
3:15
the course. So first of all uh please subscribe to this. I don't know why I
3:20
didn't uh include the link. It actually should be uh
3:27
here. Subscribe now. So I'll add a link right now. So you can do that. Uh but also there is uh yeah right now
3:36
also there is a link to uh go back and there is a link to this AI dev tools zoom camp. So this is where the course
3:42
will happen and right now we are only preparing for this course right. So we
3:48
are preparing the materials we're recording. If you want to be a part of the course there is this link here we're
3:54
registering. Um I will send it here too. So uh here in chat. So if you want to
4:02
sign up for the course too um please do this. And this is the second time we run
4:08
the course and um things move in this industry very quickly. So what was cool
4:16
one year ago today is uh obsolete. And things I covered last year um not
4:23
all of them. Some of them are still relevant but um I really want to update it. That's why we are doing this session
4:29
today. That's why we have this stream. Um, and last year what I did in the first
4:36
module uh of the course uh we called them introduction to VIP coding. I don't
4:44
want to use this name anymore VIP coding. So what I want to do is I call
4:49
it AI native developer workflow right? It's kind of more mouthful right? What does AI native mean? Developer workflow.
4:57
But I don't want to call it VIP coding anymore. Even though the name kind of stuck. Uh but what I want to show you is
5:05
the process, right? And this process is what kind of makes I don't know it's
5:10
kind of buzz word, right? What makes you AI native if you use this process, right? So VIP coding is just um kind of
5:18
shoot and forget, right? So you live only once kind of mentality, right? Right? So the agent you prompt an agent
5:24
the agent is doing something and then it's good enough. So this is kind of by coding. So what we will have today
5:31
instead of that is a process that you can follow to make sure that the code we create with a coding agent is actually
5:38
solid. Right? Okay. So that's the plan and um as I
5:44
said this is the article we can follow. What I also want to uh suggest is that
5:51
uh even though the materials some of the materials are outdated I they are still
5:56
relevant right so what we did last year in this introduction to w coding is I
6:02
did um classification of tools into different categories
6:07
um you can check this classification here I think in lessons tool map right I
6:13
don't want to do this right now uh but I still want you to go through this document. So this is something I updated
6:20
based on the uh previous year uh just to uh explain what things things are like
6:28
there there are chat applications there are AI coding assistants uh there are what I call project bootstrappers I
6:34
updated this classification a bit um so you can go uh through this yourself but I don't want to spend time on this so
6:41
what I want to do today is um I want to understand uh so first of all let me see
6:47
what you ordered. [snorts] So people want me to use cloud code. Okay. So I can use cloud code. Um but I
6:56
still don't understand what you want me to implement. Right? So I don't see any
7:02
ideas. So the ideas is like a simple project um that we can implement together today and I will walk you
7:09
through uh we will work through this project together from simple ideas from
7:14
the simple idea uh like how we turn this row idea into something concrete right
7:22
and um then we follow the process that is outlined in this article right so
7:28
this is what I want to do um so Um I don't see any ideas from there. So
7:33
I'll give you some uh time to think what you want to implement. I also have some ideas. Um
7:41
but since we're talking about uh using AI here. So what we can do? Why my
7:51
am I still audible? Okay. I don't know what's happening. Ah okay it works. Um so since we're using
8:00
AI here I can just ask Chad GPT what we can implement right and um I'll give you
8:06
some time but but um JGPT is a tool that I use
 Brainstorming Application Ideas with ChatGPT
8:12
often very often [snorts] and this is always the first um
8:18
the first step [snorts] in the process. So I see one suggestion three in a row game. So last year we had a game. It was
8:26
a snake game. Uh so we implemented a snake game together. Three in a row could be um a simple enough thing that
8:34
we um can implement. Two for weekly
8:40
feedback for projects. Okay, I like this. So I don't want to implement a game because
8:46
last year we did a game. As I said, it was a snake game. Um
8:51
so I want to I want to make some sort of application like for example this tool
8:57
or weekly feedback for projects. Uh we can see how to integrate my SQL database
9:03
to Kubernetes using stateful sets. Uh mano uh so this is not what I want to
9:08
cover here. I don't want to cover focus on technologies. I want to focus on ideas and then taking an idea and
9:15
bringing this into like implementing this idea following the process. Right? So we are not focusing on technologies
9:21
here and in fact uh of course it helps to select as we will go through the process it will help uh to use a tool
9:29
and to use a technology a piece of technology that you're familiar with. Um but here we we will be product managers.
9:37
We will be architects. Right? So we will not implement things ourselves. We will rely on agents for implementing this. So
9:44
for us the more important thing is how the work is organized. How can we make sure that the output of the agent is
9:50
correct? Right? So this is what we want to focus on. That's why technologies are secondary here. Um
9:58
so let's create an app which will analyze articles from public resources and estimate them if they can trust this
10:04
info or not. That's interesting but I think this can take some time. Uh like how can we estimate this? For example,
10:11
meeting planner with movable box for the topic and realtime target tracker
10:16
application tool for uh daily weekly feedback for personal goals like intelligent goal tracker. Okay, I like
10:24
this. Build an AI company research agent input company domain use playright.
10:30
Okay, Dominic, this is a nice idea but I guess uh for this session cuz if I'm going to use a playright, it's a bit
10:36
more complicated. So I will uh take uh okay let me check a product that somehow
10:41
fetches transactions and gives you a summary of your expenses in the last month for example. So this is a good
10:48
application but since it requires integration with something else it will also take a bit more time for this
10:53
session. Um all of that all these ideas are implementable right so everything that you mention could be applied in
11:00
this uh into this framework. So we can use this framework to implement all all
11:05
of these ideas. So what I will do now is I will select the tool for weekly feedback for
11:12
projects. So this is a good um
11:17
a good idea. Uh it's also good because it's vague, right? So if I just um if I just copy
11:25
this and uh start the coding agent, it will produce something. But like we can
11:31
just check what will actually happen. Right. Um, so let me I have multiple sessions.
11:41
Let me actually create a new one. Um, so I'm I have a
11:47
remote computer. So you don't have to have this set up. And I think we all agreed that we want to use cloud code,
11:52
right? I don't know why so many so few people voted for Codex actually. Um I
11:58
really like codex but since we are going to go with um clot code I'll use clot
12:05
code. So um I have a remote environment where my agents are running. So this is
12:11
the setup I have. You don't have to have the same setup like it doesn't matter how you set up your coding agent where
12:17
it's running. Um doesn't really matter for today's session. Right? So for me it's just simpler to use it uh this way.
12:24
So I will create a folder um how we will call it AI dev
12:33
tools experiment. So then in this tool so uh in this uh in
12:39
this folder what I want to do is um uh
12:45
see what happens if I just onehoot it. One shoot means just give it a prompt and let it implement things. Okay. So
12:53
this is the wrong one. Um, okay. So what
12:58
I typically do is I have a timuk session. So this is a remote environment. So if my connection drops,
13:03
I want to make sure that I run it in timuk. Um, so then I will uh create a
13:11
session here, t-muk session, and I use clo. So the way I start clot is this clo
13:18
permissions. So it's actually an alias uh that runs clo with the skip permission mode right. So but like you
 Running Coding Agents Safely in Tmux
13:25
just this is the usual u this is the same as clo then
13:34
roley skip permissions. So um if you're only getting started
13:39
with um coding agents, I would not recommend to run this dangerously skip
13:45
permissions like just run code in the simple way like that or codex. Um but at
13:52
some point when you interact with this it keeps asking you for things like hey do you approve this do you approve that
13:58
and it gets tiring right? So that's why I run this in the skip permissions mode. But for me also I run it on a remote
14:07
machine that um if something happens to this machine it will not affect my
14:12
computer. Right? So if you use something like code spaces or you can run the machine on EC2 or whatever you use. So
14:19
then you can be safe running things there. But in general like even for local use uh
14:27
dangerously skip permission is okay right um but at the beginning I
14:32
recommend to run it with uh with the usual mode just to understand what it's asking uh and maybe it's okay for you
14:40
okay so this is what um what I have so this is the session and I'll ask it
14:48
implement tool for weekly feedback for projects right so I don't post anything
14:54
here and uh oops. So actually I want to
14:59
stop it. So I want to have a one shot
15:04
directory. Sorry here
15:09
one shot. So now I'll do this
15:16
implement tool for weekly feedback for projects. Right. So I'm just curious what exactly will happen. Right. Um I
15:23
see a few questions why Codex is your preference. Um cuz uh you get more uh
15:30
for the same plan in Codex. So you get higher limits um usage limits. Then you
15:36
also get limits limit resets quite often. Um and the models in Codex they
15:42
are compatible comparable to um to cloud code. So, and there are some things that
15:49
work better like one of the things we are going to talk about is loop engineering and one of the
15:56
implementations of this loop engineering is the /go command. We will see it later. In my
16:02
experience, it works way better in codex than in code. But for most of the cases
16:09
they are compatible and also um we will do this in a tool agnostic
16:16
way right so it will work what we do today will work with any coding agent so if you use codex it will also work so
16:22
you can use codex you can use open code you can use whatever coding agent you prefer
16:29
okay so it will implement something So you
16:36
decided for uh for stack. So yeah I I'll just leave it alone. But then what I
16:42
want to do in parallel is [snorts] I uh want to create specification. So here I
16:47
am in this section right now specification before code. Um because um the problem with uh this one short
16:53
implementations is when we give it little prompt the model uh the agent has to make a lot of assumptions right. So
17:00
it does it didn't ask me anything right? So it didn't ask me what tool stack I want to use. What is this problem I want
17:07
to implement? Like it didn't ask me any of this stuff. And this is a problem
17:12
because it cannot read my mind, right? And perhaps I had something on my mind
17:17
that um the agent will like I didn't express
17:23
it properly in my prompt. So the agent will fill these gaps and the decisions
17:29
it will make it will most they will most likely not be what I had in mind right
17:34
so that's why we want to first build the specification so this is the first step in our process we want to make sure we
17:41
really scope uh out the problem or how to say scope yeah so we define the scope
 Creating a Feature Specification Before Code
17:47
we really understand what we want to build and uh there are two level of
17:52
specifications um project level so what exactly this project is about and
17:57
feature level so this is more like uh for each task so we are starting with the project level um specification and I
18:06
really like using charg for that so you can use any uh AI assistant here and I
18:11
usually use the browser you can of course uh go here and talk it's it's fine but um
18:18
I prefer this way I also prefer uh doing this because usually I don't do this on
18:25
my computer. I use my phone. So I just open JGBT on my phone and I start doing
18:31
a brain dump. So I really like using dictation mode and this is what I will do.
18:37
So I will say um I want to build this tool and I want
18:44
to help me I want you to help me scope um to set the scope for this project. So
18:51
I want to be very precise in what I want to build. So I want to brainstorm with you uh and understand how the uh tool
19:00
should look like. So give me some options and ask me some questions.
19:06
And so now what I want to do is I want to turn uh this wake prompt into
19:11
something very specific. And here um I usually don't put like a lot of u the
19:19
thinking mode is not like very high. So something like medium is okay. Um cuz
19:25
like first of all it takes too much time. Like if I increase the thinking mode like let's say if I go to high
19:30
extra high it's thinking too much. Um right? So I want to have something more interactive.
19:37
Um, and then also like these uh thinking modes, they are uh very verbose. Like
19:44
even this one to be honest is very verbose. So I wanted it to uh let me
19:49
actually do this. Ask me one question at a time and keep
19:58
your output short. Right? If I don't do this like I'll get a wall of text and
20:04
then I'll have to read through this text and it's just difficult.
20:09
Okay. So this is what I wanted right so I wanted to have a very simple thing. So
20:16
who gives the weekly feedback product owner team members client stakeholders external testers?
20:22
Um so the way I see I don't know maybe the person who decided on this idea can
20:28
correct me uh but I think we best better if I just make some assumptions these
20:33
assumptions might not align with what you had in mind but still we will be moving towards something that we decide
20:40
not the agent decides right um uh I want this to all team members not
20:47
just product own project owners uh I want all team members um to be able to
20:54
contribute it to to this uh contribute the feedback and uh then perhaps we can
21:02
have something like a retrospective uh where we can discuss this uh feedback.
21:10
So I I just made an assumption that we as a team have these processes and then once per uh I don't know some time once
21:17
per month we have this retrospective where we talk about things that go wrong
21:22
things that work things that don't work things like that right so what should each team member submit every week
21:30
um yeah start stop continuous looks like a
21:35
nice uh framework so we want to talk about things that work, things that don't work. Um,
21:43
yeah. So, I think this should be uh the first should work fine.
21:59
Should feedback be anonymous? Um,
22:04
yeah. Uh let's uh let each contributor decide. So they can um submit things
22:11
anonymously. Um but also they can choose reveal their name by default. Let's make
22:17
it um attributed but then they can tick a box uh submit anonymously.
22:26
I think it makes sense, right? So if you want to give some critique maybe you don't feel comfortable
22:32
talking about this um in person I I don't know like it depends but let's
22:39
just go with this right so it might be awkward a bit uh and then uh during the actual retrospective uh probably
22:45
everyone will understand who that person is who gave feedback um but maybe for
22:51
some things um like it's okay to uh to have this possibility
22:57
Um, next question. When should teammates see submitted feedback?
23:03
Okay, they only see the feedback they submit uh but the project uh
23:10
okay I actually need to think about this um immediately
23:15
when the collection closes only [snorts] during the perspective.
23:21
Yeah, let's uh go with the option number four. So when I submit I only see uh
23:26
only see what I submitted. I don't see the submissions on of others.
23:38
Okay. Uh Yogen uh I don't know how if I pronounce your name correctly. Um all
23:45
team members right. Okay. So I hope I'm moving in the direction you uh wanted.
23:50
Who can reveal and facilitate the feedback?
23:56
uh that's the facilitator number two which probably is a project
24:02
owner. So I I guess you can see the idea right. So we want to be very precise in what we
24:10
want to build but more like from the user point of view like we are not talking about technologies here. We are
24:16
not talking about implementation detail but like more what exactly the tool should do not how
24:24
um how feedback should appear.
24:29
So uh all feedback should appear at the same time and then during the meeting um
24:36
yeah we cluster there should be some automatic clustering but also during the meeting uh as the first step we cluster
 Defining Retrospective Features and Voting Rules
24:41
them um and then um once the cluster them also
24:49
each team member can vote for the things that we can talk about. So then uh at
24:54
the end we have a prioritized list of things we should discuss in the retrospective.
25:15
Okay. Um next question. How many votes should each person get? Um
25:21
three is fine. Uh should people be able to place uh
25:29
yes like if somebody really wants to talk about something uh at least in
25:34
retrospectives in companies where I work usually uh you could vote for the same
25:41
topic multiple times. What should happen after the discussion?
25:48
Yeah, [snorts] let's just capture both actions and decisions. uh we can also do like I I don't think
25:57
we can actually like what should happen after the discussion capture um
26:03
ideally if we record this meeting right so then uh we can use AI to um
26:11
automatically infer this from the transcription uh so let's uh capture actions and
26:16
decisions and also we want to record the entire meeting so then uh at the end we
26:22
can upload the can get the record uh transcribe it and then based on the
26:28
transcription we can capture all the things and uh all the actions and decisions.
26:47
Um so now let's go with a simple version.
26:53
We just upload video or we just upload audio or transcript directly right and
26:59
then it can process it and then uh as the then we can add other things on top
27:05
of that when we need. So let's not let's not do um built-in recording yet. I just
27:12
don't want to be very ambitious here. Right. uh at the end we can build
27:17
something like that right but um we just you know go with the simplest version
27:24
who confirms the extracted solution decisions
27:30
um I I don't know like I'm tired of making decisions um okay I'm to be
27:35
honest I'm tired of making decisions I think this should be enough for the MVP
27:40
um for the rest of the important things. Uh, I want you to make some decisions
27:46
and explain me why you chose this decision, why you decided to go with
27:51
this option and what were the other options you considered.
27:58
Like at some point like we can reply to these questions all day long, but it's been already half an hour and we are
28:05
only getting started, right? Um,
28:11
okay. Weekly team feedback tool. MVP scope. Um create feedback cycle. Collect feedback.
28:19
Uh reveal and cluster feedback. Vote on discussion topics. Run the discussion.
28:26
Discuss. Keep deferred. Process the meeting recorded. System generates a
28:31
transcript. Okay. Decisions made for the MPP instructed results require facilitated approval.
28:39
Okay. So then somebody goes through these things after this feedback is submitted as a separate card
28:46
team can create okay anonymous feedback stays anonymous
28:53
yeah voting is visible after voting closes yes I think it's good that people
28:58
don't see you where other people are voting in reality when you have a pipboard you cannot not see right but
29:05
here maybe it's a good decision automatic clustering is always editable.
29:11
Okay, good. Action items have a simple structure. Uh description, owner, optional due
29:17
date, action items. Yeah, as a result of the meeting, we want to have action items. That's cool. One retrospective
29:24
belongs to one project. Okay. Main screens, project page, current feedback
29:29
cycle, perspective, feedback form, retrospective board,
29:34
media, upload page, retrospective summary, roles, team members, facilitator.
29:42
Okay. Then things that we explicitly exclude from MVP. I think this is good. Like we decide what is in the scope and
29:48
what is out of the scope. Like with MVP, we want to have a very focused thing
29:53
such as success metrics, MVP definition. Okay. So now
29:59
you can probably interact more with this but I think this is enough for to get started. Now I write save everything to
30:06
a markdown file that I can download. Right. So this is how I always
30:15
uh finish these brainstorming sessions. So what is doing is writing some Python code or creating producing this file
30:22
doesn't really matter. What matters at the end is I will have a markdown document that I can download. Um, in the
30:29
meantime, let me see what this thing did,
30:34
right? Uh, is there a dependency Python CLI for tracking weekly project health?
30:40
Uh, okay. So, it did something completely different, right? So, it did
30:45
a CLI for tracking weekly project health. Okay.
30:51
Um so project at API name building API onexi.
30:57
Okay I small command line register the project you care about local short entry
31:02
per project per week and get a digest you can paste into weekly update.
31:08
I mean it could be useful right um but this is not what we wanted at least uh
31:14
you can see my point right. So this is a very different thing at the end very
31:20
very different right so you just made a lot of assumptions and it just went with these assumptions I didn't stop it I
31:26
didn't ask it to uh I didn't correct it so then the result is a working app but
31:31
this app is absolutely not what we need right so I'm going to stop this um and I'll
31:40
create another directory which I'll call um
31:46
project heatback. So this is will be actually our directory that we are going
 Reviewing Outdated One-Shot Code Implementations
31:52
to use and I'm going to open it in visual studio code. You can use whatever
31:58
like if you use cursor you can open it in cursor. If you use oops if you use um
32:05
yeah whatever you use you can use it. So now I will open it
32:12
as a project and right now there's nothing right. So I want the first thing I want to create will be an empty folder
32:19
called docs and what I will put in this document is
32:25
uh in this folder is uh this thing.
32:30
Okay. Can I download it? I can also read it. uh but we already
32:37
read it but I'll I'll read it not here. I'll read it in uh
32:44
here. So um I should be able to just drop here and
32:52
I'll call it what? Yes, I'll call it plan.
33:02
Okay. So let me commit it. I think I'll just use uh here the
33:09
terminal get status. Uh so this is not a repository yet. So I do get in it and I
33:17
do get at g commit u
33:22
md right. So this is our document. So you you should commit regularly.
33:32
So the reason I add underscore here is because we can have some other do some other folders in our uh in our project
33:41
right and then I want the important kind of uh uh important folders to be first
33:46
in this list so then I can see them immediately. Can you drop down here the MD file? I
33:54
think I can. So I what I will do is um I'll ask clot
34:02
um upload the plan MD file to G.
34:10
So, and I'll actually I wanted to edit this a bit, but maybe we edit this and I
34:16
also uploaded. I could have also actually committed this to GitHub already and share the
34:22
link with you. Um maybe it would have been better, but it already created the
34:28
G. So I will just give it to you.
34:34
But if you're watching this in the recording, there probably be there probably will be some folder that I will
34:41
put inside our AI dev tools zoom camp. So here in overview I will probably
34:48
rename this. It will be not overview but something else. But inside we will have code and then uh I will put the code
34:56
that cloud code created when we didn't have any specification just for you to
35:01
check it and I will also put all the other artifacts we produced
35:06
okay but this is this is it right so and this is very similar to what we saw
35:12
right this is actually exactly the same document that we already reviewed so
35:18
here there's nothing to review uh already Yeah, because we already reviewed so there is nothing left to
35:24
review. Okay, so um this is what we did starting a chat chat assistant. Um
35:31
now we need to initialize the project. So I already we already bootstrapped it. Um
35:37
and then I want to do this. So we didn't agree. So I'll
35:44
start a new session. So we did not agree on the technology, right? Uh so we did
35:49
not discuss the tech stack. This is something we could have done um we could
35:55
have done um during the brainstorming session with the chat application. Um
36:02
but usually I already so I use these chat applications for conceptual thinking like what exactly I want right
36:09
and then um you don't have to use you can use any you can also use a coding assistant for that but for me it's kind
36:16
of helps with separation of concerns kind of because coding agent cannot I'm sorry AI charge cannot really touch any
36:24
files right so it kind of forces it to stay on the conceptual level rather than
36:30
create code so it will not create code unless you ask okay now I'm copying this read plan
36:37
propose multiple options for the text t and explain each option don't write the code yet so we want to just understand
36:43
what we will implement
37:00
So now it's looking for um this file it found to uh plan.
 Evaluating Technology Stacks and Framework Trade-offs
37:08
So now it will read it and it will actually say okay now I understand what
37:14
you want. So uh before the options here's what actually drives the choice or hard parts
37:21
retrospective word media pipeline uh audio video uploads
37:27
transcription and the so for video for media pipeline I think
37:33
what we can do is so for example I have u an Android phone on this Android phone
37:39
I have a recorder so this is just usual Google recorder And what it can do is I can just use my
37:47
phone to record the conversation. So let's say we are um talking we're
37:54
sitting in the room. So we have a TV screen uh and then everyone is talking about these things during the
37:59
retrospective. Let's think let's say this is not a remote one. So then at the end my Google um will create a
38:07
transcript my Google recorder right? So then I don't need to do this media pipeline. Maybe it will just help uh
38:13
make things easier. Um although if I think about this like just sending this thing to um
38:20
uh to whisper shouldn't be too difficult, right? So maybe I'll just leave it like that. Uh transcription
38:26
that takes minutes needs direct to object storage upload plus.
38:32
Okay, whatever. I guess it works. Uh lamb steps clustering cards extraction
38:37
decision a sync provider agnostic small amount of code anonymity. Okay. Option
38:43
nextj full stack plus postgress.
38:50
Okay. Um junga I like junga to be honest like um I
38:57
think this would be a better option if we wanted to use like something like uh bersel for hosting. It would be really
39:04
good option because in versal you get out of the box you get many things out of the box. H yeah it even says versal
39:10
serverless model can't ah so yeah it even suggests that deploys this is good
39:17
but uh for me I can read JavaScript I can read Typescript but I'm not uh I'm
39:23
still like I really have to focus for me when I open the open Python code for me
39:29
it's way easier to to read the code. We're not going to read any code today. That's why like you can just choose
39:35
whatever is more comfortable for you. Um then I like like jungle more than uh
39:42
fast API. Um because I know it better, right? I
39:48
know it better than uh fast API. So I would just go with the technology that I
39:54
know. So I don't even live life elixir. Okay, that's uh that's very interesting.
40:03
Um kind of exotic, right? Why did it uh
40:10
suggest this thing? I don't know. And it says time to MVP with jungo is
40:16
fastest. Okay, like I was kind of leaning to this, but now uh since we
40:22
want to move fastest, we don't have a lot of time on this section. Um, and it says recommendation option B. Um, yeah,
40:30
but I would still make my own suggest uh option, right? So, if you're like, okay,
40:35
I don't really care. I ask clo or I ask Codex based on what you think what is
40:41
the best suggestion or you can outline some um some ideas like where you want
40:47
to host it and things like that, right? And then it will help you to to decide. For me, uh let's go with Jungo. I like
40:54
Jungo. I have many websites uh that are implemented in Django. So for example uh for our courses we use this platform. So
41:02
this is Jungo. Uh then I also run uh this community AI shipping labs. It's
41:07
also Jungo. So I have experience with Jungo. So for me this is [snorts] a natural choice because I already uh is
41:15
familiar with this. So I see a comment fast API plus React. So if Alexi uh
41:21
wants to use that um use that right. So here we're not really um it's not really
41:28
about technologies, right? So any of these options will work. I wouldn't go with this Phoenix though.
41:35
Um because it's very exotic.
41:41
I don't know why why Alex here. Like I would go with Rust or go if I
41:48
really wanted to do something like unusual. Okay, let me lay lay out the concrete
41:56
architecture. I will write it to doc architecture even though I didn't tell it uh to write it into file. It made the
42:02
right call. Uh I would eventually ask it like after we discuss all the things I would say at the end of the session, hey
42:10
like let's now document everything. I didn't need to do this. It just made this decision itself.
42:17
Okay. So it's taking some time to do this. Let me see what we have. So, so,
42:23
so far we don't really have anything, right? So, LA is the only um document we have. I'll also tell it to
42:32
commit after we finish. Commit after you finish.
42:43
So, language Python 3.12. I would go with Python 3.13
 Choosing Django and Defining MVP Constraints
42:51
but I don't think it matters posgress I think right now it's version 17
43:01
let's go with Python um with last Python
43:07
and posgress because I think last one is this 14 that
43:14
junk templates alpine js I have no idea what is But
43:20
I will like when it comes to um front end technologies I'll just trust
43:26
agent to pick up whatever want uh authentication email uh plus invite
43:32
links. So I want to a bit the scope it so I don't want to um go like full um
43:41
like I don't think we need these things right now. Let's make out very simple.
43:50
No emails here. And then background job plus radius. Um
43:59
this is too heavy. Uh file storage.
44:06
File storage. We don't need file storage.
44:13
Process recording. and throw it away.
44:20
Uh, deep gram API. So, I have no idea what's that. Let's use whisper from open
44:28
AI llm of course because I use clo cloud
44:33
code it suggested uh this you use open ai too
44:42
deploy um let's remove that part and only include
44:51
docker compose right so I want to disco cop it a little bit so it's more implementable.
44:57
Um in the text stack we talk about
45:04
trade-offs too. Yes. Um and this is what I'm you you still need to like I I think
45:10
of myself and uh this is what I want you to also do of I think of myself as a PM
45:17
a product manager plus architect. Right? So product manager is thinking about the
45:22
think from the user point of view and architect is thinking about technologies from high level right so you don't
45:29
really go and implement all the single all these things by hand but it helps to
45:35
um to be aware of the technologies and trade-offs you're making right and let's
45:42
say you don't have this experience right uh that I do so I already for me this is
45:47
not the first time I do this kind of things, right? So for me, I already know what I want to do like what kind of
45:53
technologies I want to use. You might not have this background. You might not have this knowledge. So then what I
45:58
would suggest is to challenge every single line of this decision file here
46:05
and ask, hey, do you think this is good? Are there um newer versions? Because we know that
46:11
LLMs have this knowledge cutff. So they suggest so for example it suggest to use GPT40
46:17
while we have P4 P46 right right now. So
46:22
um I would actually challenge every line here and ask hey do you think this is a
46:28
good idea like is it complicated or not? Can there be simpler versions? Right? So I would
46:34
really ask I would really challenge here every single line.
46:41
Um okay so what I also want to do is um
46:46
I like using dictation mode here too. So this is what I do. So I'm on Windows that's why if I press window key plus H
46:55
I have this thing right this this is a transcription. So um I want you for
47:01
every single line of your technology choices I want you to see if there are newer versions available for that
47:14
file transcription is unreoverable the media is already gone or whatever like we don't worry about this things um we
47:20
will deal with them later as we um
47:27
as we make it let's say more mature for MVP key. We don't need most of these things.
47:34
January 2026. That's interesting because for O was released like 2 years ago. So
47:40
I think it's kind of lying. Or maybe it just didn't want me to use it like a proper OpenAI model because
47:46
it's an anthropic uh model. Okay, I'll let it do it, but then I want
47:52
to continue. Uh so what do we have next? So next now
47:58
we have the text tag and now with this now with this text stack and uh
 Generating a Structured Task Backlog
48:07
with the plan I want to create a backlog of tasks right so what I want to have is I want
48:14
to take like everything that we did here plan architecture all these things and I
48:20
want to take them and put them into uh a list of tasks such that each task is um
48:30
what do I say here? Each task is independent, small enough to finish in one session. So it shouldn't be too big,
48:36
shouldn't be too small. Um so I want to have like a very clear decomposition
48:43
and I think after this session I'll need to update this article a little bit, right? Because like we have uh selecting
48:50
technologies like I spent a lot more time on this than just this prompt. Okay. So, uh now I will probably do this
49:00
continue doing this in the same um in the same session. I think it's busy
49:07
with checking the technologies. I think it's okay.
49:13
Um so I don't want it to like go crazy with like all these choices.
49:19
So uh now uh I continue doing it in the same chat because it already has some
49:24
context about um what we want to do. Um so I'll just continue. Uh alternatively
49:30
you can start a new chat. It's also not a problem. Um but first please commit what you
49:39
have. Uh it's is it time to update the
49:46
application spec? Uh uh Alexa asks I don't think it is right. So the from the
49:52
user point of view um it didn't change much right. Um but
49:59
maybe yes some things like some things we did uh here we decided here they do
50:05
influence the decisions we made.
50:10
And I see that it didn't update. Uh I also see that you didn't update
50:17
our architecture MD. Please do this before you commit.
50:24
So it could be like uh when architecture things that we decide in our architecture they can influence our
50:32
original plan our original spec right so then of course we need to update it. Um I don't know if um anything we did
50:41
actually uh all the decisions we made here influenced this. Um so for now I'll not
50:49
uh we can actually combine these files too right we can take the architecture plan
50:56
put them together
51:01
um okay it's producing a backlog of tasks okay it's
51:07
fine so uh let's see tasks
51:19
Project skeleton with a passing test. Um, okay. Docker compos environment.
51:26
Okay. Base layout and front end assets. Okay. Authentication without email. Uh,
51:32
project membership join. Ah, I think Alexi what you meant is like this decision that we made about authentication without email, it does
51:39
influence uh the original spec. That is correct. Right. Um so it does help to um
51:48
keep this in sync but for me this plan and task and architecture. Um so they at
51:54
some point they will um kind of say disynchronize with the actual content.
52:00
So I mostly use it for seeding the tasks these tasks
52:05
uh and uh to be honest I don't really go back to this file often. So uh in the in
52:13
the article I included did I include it? Yeah, this um
52:21
SQLite search um like the the way I approached it and um
52:29
there I followed the same process right so I created uh I talked to JPT then I
52:34
defined what I want to build and then uh I think yeah I have plan here in the
52:40
root and actually this thing kind of disynchronized
52:47
from the codebase So I just used it as a starting point and then like I can just
52:54
actually delete it right so it's not really needed anymore because many many things happened since this file was
53:00
created so like what we can do is we can treat this files right now as just seeding
53:05
uh point kind of like we will create tasks from this and then um
53:14
yeah we will not need to actually update this file all the time, right?
53:20
So, at least I don't do this. Sometimes it can help uh but for me, we have this
53:25
uh these tasks and this is what matters right now because we can take these tasks and actually uh
53:34
and actually start um yeah working. So, we have the tasks. This looks
53:42
reasonable. Authentication without email. Project membership and join leaks.
53:47
Uh user can create a project and invite others. Permission. Uh feedback cycle,
53:56
feedback cards. I think it looks okay. Um like each of them is a concrete feature with concrete
54:04
goal and concrete description. So it doesn't seem too small. I'm not sure about this. um some things like
54:11
permission predicates uh but I I will just go with this right
54:16
so to me like here you need to wear your kind of product management manager hat and understand uh
54:24
like is this task good enough like is it not too small not too big and you think more about like from this from the
54:31
product perspective not from technical perspective um okay so we have 28
54:41
uh things here. Okay. So now what we want to do is we
54:47
want to put these things into GitHub, right? So they are here but this is not
54:53
really useful. So the the reason I asked it to put this into the um to the
55:00
markdown document is because I wanted to review it, right? But once these things are done, now I want to put this to
55:05
GitHub. Um, so I'll just do clear. I'll start a new session. And in this session, I want
55:12
to so I'll just dictate. So I want to publish this project on GitHub. Uh, but
55:18
I don't like the name. Can you please help me select the best name for our
55:23
tool that we're building? You can check plan.md uh to see what exactly we're building.
55:28
So um yeah, I want to have a nice name that reflects u the purpose of the
55:35
project.
 Repository Creation and Pushing Tasks to GitHub
55:42
Okay, let's see what I suggest and then we will uh create um
55:48
I also want to check if yeah get lo. So we
55:57
we already have uh some things here.
56:04
Okay.
56:09
So, what is it doing exactly? Weekly loop. So, why why it was doing
56:14
this retrol loop retro cycle?
56:24
I don't really need an organization. I don't need an organization. And I just want to create it in my personal um
56:33
space, right? So just um suggest a name. Uh retrol loop is okay. Uh so let's do
56:41
this. I have a skill for creating GitHub repo.
56:48
Like if you don't have this skill, like you can just ignore that it exists. Um
56:54
but yeah it your agent will do the same thing without the skill. So for me it's just I have a flow for creating um
57:02
projects but yeah just pretend sorry pretend you did not see the skill.
57:13
So create make it public.
57:29
Okay. So now we have this repo. I'll share it with you.
57:37
So for now we don't really have much here. noted it mean no license whatever no I
57:44
don't want to do these things uh actually it can do this by itself even
57:50
if you don't ask it so at least here it it asks okay so what do we do next we create a
57:57
GitHub issue for each task
58:03
tasks MD so I quite often um start a new session
58:13
because um so first of all you're kind of you're spending tokens right so every
58:19
time you continue a session um you have a new task but you continue a session
58:25
from the previous task um not only like there's already some context so it can
58:31
um make your model um can confuse your model um but also
58:39
you're spending tokens right So like for each new task I try to start a session a
58:45
new session. So now it's going to create issues. So
58:53
it's creating a script. Um and it's running the script. So I think if I go
59:00
now to this retrol loop
59:06
I see this issues here.
59:12
I don't know why I decided to add the t the the number here. Um whatever. Like I
59:19
would like on the real project I would ask it to uh remove the the numbers
59:24
because makes no sense. We already have a number here. Okay.
59:31
Um clear
59:40
so uh implement task number one. So now we want to bootstrap the project. So we
59:47
want to actually um create uh what where is it? Let me close all these things.
59:58
So we want to implement um the things
1:00:06
okay. So this is what I do. So we create the
 Bootstrapping the Project Workspace
1:00:12
first task. So this uh bootstrapping actually took more time than I expected
1:00:18
but this is time um so this is time well spent. Uh so I think I will take more
1:00:25
time than I initially planned. So I planned initially to do it for 90 minutes. I think it will be more like towards two hours.
1:00:35
Okay. So it's working on this thing right now and while it's doing this um
1:00:45
so I want to move to context engineering. So context engineering is
1:00:50
um so first I want to start with prompt engineering. So prompt engineering is
1:00:56
the prompts you write here implement task number one right and then uh when you do this when you start a new session
1:01:02
the agent needs to every single time the agent needs to figure out what exactly I want from it like what is the task
1:01:08
number one where it is uh what do we use uh do we use GitHub for this so it needs
1:01:14
to um understand what exactly is happening right so in this case um well
1:01:21
I don't know exactly where it took Task number one. So I think it found it.
1:01:30
Yeah, I think it found it this uh in task. So it didn't even go to um
1:01:38
it did not even go to um our uh tracker, right? Um so agent is making assumptions
1:01:46
here. um what I wanted it to do to actually go and um
1:01:51
take this issue from um GitHub. Right? Then I see uh some other things.
1:01:59
So um where let me check what it's doing.
1:02:08
So it was checking versions. Uh then it used Python 3.14
1:02:16
uh EVP index. Okay.
1:02:26
Yeah. Here everything is fine. But um usually so when we start a new session
1:02:31
we want the agent to understand what is happening and what it needs to do because if we just give this simple
1:02:37
prompt this is not enough. Right? So then our prompt should be more explicit.
1:02:44
I should have said implement task number one which is a GitHub issue. Um and then
1:02:50
maybe add more things. So for the agent not to think about these things all the time, we need to do what we call context
1:02:58
engineering, right? So we need to give the agent the right context. And uh most of the time context engineering in case
1:03:04
of coding agents is about creating this file called uh agents.mmd. So I'm going
 Context Engineering with AGENTS.md
1:03:10
to create it here and write in things that are important
1:03:16
for the agent um in this file. So this is just a simple markdown file where we
1:03:21
describe all the things that are important for the agent like what are the um
1:03:28
what are the tools that we use. I think I have an example here. All right. So
1:03:34
comments uh tooling rules uh constraints pointers to documents and things like
1:03:40
that. So here I have an example. You see in this example I don't use any uh
1:03:45
markup. So I don't use uh any u like headers. I don't use bold formatting cuz
1:03:51
this is not really needed. So um what I will do now is I'll take this example
1:03:59
and I will ask uh is it done? No I think it's still doing. So after it's uh it
1:04:06
has finished so I will ask it to create agents uh MD file with the this example
1:04:16
from this example um but um since here I use clot I don't
1:04:22
use codex so codex would go and read agents but clot does not clot needs a file called clot md and I use both I use
1:04:31
both codex I use clot code I use other agents Um so only for CL we need to have like a
1:04:36
separate file. I want to make it possible for me to use any coding agents. So let's say I'm using clot and
1:04:44
I run out of limits. So then I can go to codex and continue what I'm working on. Right? So I don't want to really u go
1:04:50
between different agents. So I want my setup to be uh tool agnostic. That's why what I do in cloud is I have this line.
1:04:58
So this is the single line I have in my cloud code. It says, "Hey, go read agents.mmd." Right? So then it goes and
1:05:05
reads it. Okay. Um
1:05:12
test exists version. Okay. Commit and then create agent um and then
1:05:20
create agents MD with uh content similar to this.
1:05:29
And I'm doing it in this session because it already has some context about what we um want to do, what kind of
1:05:36
technologies we use, how to run some things, right? So the next agent does not need to rediscover these things. It
1:05:41
will not need to rediscover. Okay, this is jungle project. Okay, we use UV for testing or for for dependency
1:05:48
management. Uh so it will not need to rediscover this. um it will just get it
1:05:54
from agents.m MD. So it flaged some things but I kind of
1:06:01
need to move faster that's why I am ignoring this. You shouldn't you should
1:06:06
actually read and see what it wants and then like if it's not clear you just ask
1:06:12
it hey what do you mean here like what do you want for me like what kind of decision you want and sometimes uh in
1:06:18
many cases uh you don't really need to decide you can ask hey what are the possible options
1:06:25
and then you ask it what is the best one and then you just say okay let's go with this
1:06:33
and Um from what I see it added so this one is not really needed
1:06:41
right uh jungo app for weekly stop start continue cycles and resp perspective the
1:06:46
whole so this one we don't need
1:06:53
then I don't like uh this extra um extra markup because it will cost us
1:07:00
tokens UV sync [snorts] uh run server migrate
1:07:06
pi test rough check okay
1:07:12
um I would actually also create a make file but this would be separate thing all uh authorization leaves here uh
1:07:24
okay it kind of becomes big I don't know like do we really need uh
1:07:30
do we really I will just dictate uh do we really need all these rules? So
1:07:36
the idea behind this file is that every agent session that starts in this uh
1:07:42
repository needs this information. Do you really think that all the agent sessions will need that? Keep only the
1:07:48
most important ones and then also like I'm not sure how
1:07:56
important is this thing, right? uh if agent needs to know what is uh what we're talking about it can just go here
1:08:02
and I think it's just duplicated this and I'll remove this from here too I
1:08:10
think uh our readme for readmi I have a several separate process how what should
1:08:16
go in readmi and it should be different from agents and actually uh since we are
1:08:21
already on my substack I have an article about that
1:08:26
Um let me go to archive. How to write a
1:08:33
good readme. Right. So this is a separate thing. Um I would like read me
1:08:39
and agents MD. They are very different files.
1:08:44
Okay. So now it uh
1:08:50
so then agents sometimes they write things that do not exist. So they say
1:08:56
okay we only have posgress we don't have this but what is the point of writing what we don't have right so then I
1:09:02
usually trim this
1:09:09
okay so this is our uh agents MD so next time when we create a session uh it will
1:09:15
know um it will get this information uh but the important part is we also need to
1:09:24
um to say that things are in uh in in these issues, right? By the way, I think
1:09:30
we should close this one. So, I'll just close it.
1:09:35
Um so, um we need to say this is the process we follow. So, for this I
1:09:42
usually create a document called process.md. So, I will put it here
 Defining Process Guidelines and Workflow Rules
1:09:49
process.md where I describe the process. So, right now it's very simple. So I just say uh tasks are in GitHub uh read
1:09:58
the acceptance criteria. This is something that we will add later. Um, and commit regularly, right? So maybe I
1:10:04
don't even need this right now. Um, so this file will grow but I want to see
1:10:11
the file because this is the process. This is how we work. So this is something that agents if we want to
1:10:17
implement something or do something the agents will read this file and I refer I
1:10:22
don't we can put them here in agents.mmd but because I know that uh this file
1:10:27
grows uh and then for these files as I said uh
1:10:32
they are more like um things that I use for seeding the tasks right so for me
1:10:38
they are more like one of things that I that will became stale that I will want
1:10:43
to eventually remove. So there is no point for me to mention these things. So then what I will do is I will uh add a
1:10:50
section called files on documents.
1:10:56
Um so right now um we don't have this. So I think this is just example. So
1:11:02
typically I have a lot of different documents here in the docs that describe
1:11:07
okay what is the process how to write tests how to uh work with API how to
1:11:15
design UI and so on right so each of these things each of these as aspects is a separate documentation file and then I
1:11:22
link these documents in agents.mmd so then if a task is about
1:11:28
process is about implementing something then it goes and reads the process. If the task is about fixing tests, it goes
1:11:34
and uh here and reads the testing guidelines. If the task is about UI, it
1:11:40
goes and reads about our design system. Right? So it helps our um so we don't
1:11:47
put everything in agents MD. So we um here we manage our context in a way that
1:11:52
the agent knows that these files exist and if it needs for this specific task it knows where to find for the
1:11:59
documentation for implementing this particular task. Right? So um right now we keep things simple. So we only have
1:12:06
process and the process is this right tasks are in GitHub
1:12:12
uh one at a time. I don't think it actually matters here. Okay. So let's commit
1:12:22
commit and push.
1:12:29
So this is our context engineering. And the next thing we need to do is we need
1:12:35
to do something with these tasks. So okay this one is done but task number two
1:12:41
is docker compose. Okay, for docker compost this is a technical task but um
1:12:47
here let's say uh I want to take this one
1:12:53
uh this authentication. So here I want to have a tasks that is very clear. So
1:12:58
there is still some room for ambiguity here. I want to remove all possible room
1:13:03
of all possible ambiguity for the tasks that we have. Right? Right? So I want to
1:13:10
have the tasks to be very precise and I want to read the tasks to understand
1:13:17
that if this task really aligns with what I want because if it doesn't the agent will make assumptions and these
1:13:23
assumptions will not necessarily uh match your expectations right and then
1:13:29
it will implement something that you don't need right so that's why again speaking about specifications uh we were
1:13:36
talking about specification on the project level and we did all this uh talking to chat GPT uh thing right in
1:13:43
chat assistant but there are also feature level specifications so this is exactly for tasks so this task I want
1:13:48
now to take this task and make it very crisp I want to make it very focused I want to make it as unambiguous as
1:13:55
possible right so then when an agent is taking these tasks it doesn't need to make any decisions it doesn't need to uh
1:14:03
it just can take it and implement it right so then of course technology choice is not something we have to
1:14:09
specify here. We can but it doesn't have to be here. Um so the agent may still
1:14:15
need to make some decisions but these decisions should be decisions about userfacing features right and uh in real
1:14:23
teams we typically have product managers who are responsible for the function functionality like from the user point
1:14:29
of view like what happens if you click this button right uh or what is the um
1:14:36
the the task the user is trying to uh to do to accomplish with um our
1:14:42
application. Right. So that's why um so what typically product managers do is
 Task Grooming via Product Manager Persona
1:14:48
there is a process called grooming. So they take an issue that looks like that and they groom. They make it more
1:14:53
concrete. They make it more they make it less ambiguous. And um what I want to do
1:14:59
is I want to turn this into uh something that looks like
1:15:06
this. Right? So there is a goal, there is acceptance criteria uh and things like that. Right? So I think I should
1:15:12
also we should also keep um description here. It helps but we want to add other
1:15:19
things right what is uh what are the acceptance criteria and what things that we don't want to implement right so we
1:15:25
want to also be specific about things we want to implement but also about things we don't because otherwise the agent will think okay it's a good idea let us
1:15:32
do this right and then it will come up with something that we don't need at least for our MVP and then we have more
1:15:40
code to maintain okay so we need a product manager for that right so typically this This is the
1:15:47
what uh um in teams the setup uh we have
1:15:52
is uh product managers take issues like that and turn them into something that
1:15:58
engineers can just take and implement without bugging the product manager all the time.
1:16:03
Okay. So now I want to create a folder called team and in this folder I want to
1:16:09
create a PM. PM will be our product manager that will
1:16:15
take a task and it will turn in it into something that um agents can implement.
1:16:21
Right? So then this is the description for our product manager.
1:16:27
So you're a product manager. You groom a task before anyone implements it. Read the issue. Uh rewrite it using the
1:16:33
template. I will now uh create the template too.
1:16:39
So this is our task template. I think I'll um also create old dated documents.
1:16:47
So we don't need this architecture anymore. We don't need uh plan anymore.
1:16:54
We don't need tasks anymore. So for now I'll keep them in the project but eventually we can just remove them uh
1:17:01
because we already have issues. Um so the this is enough for us to to
1:17:07
continue. Okay. Um although at the beginning we
1:17:12
may still need plan for the agent for the RPM to groom right so to actually
1:17:17
not make assumptions about something we already talked about. Um but again so
1:17:23
read the issue uh rewrite it using the template.
1:17:33
Okay. Make themselves criteria checkable. Someone should be able to point at the
1:17:39
screen and say yes or no. Think about the age cases. Uh the person
1:17:44
who filed uh it did not. Okay.
1:17:50
Um but the important thing here is this acceptance criteria, right? So how do we know that the task is done? Right? So
1:17:57
this is what we want to be very explicit and this is very helpful for the
1:18:03
engineers. Right? So this is yeah kind of similar to functional nonfunctional requirements. There are different um
1:18:09
frameworks for this like this is just the one I use. I also often use user stories like when uh then uh kind of
1:18:18
framework like uh as a user uh when I want to do this uh I do that right so
1:18:24
these kind of user stories or sometimes you can also like when you're thinking about specifications you
1:18:30
can also think of jobs to be done framework there are many frameworks right so but um agents know all these
1:18:37
frameworks right and if you have some product management experience or I don't
1:18:42
know so some UX experience whatever you can use that like you can just tell the agent what you want to do and then it
1:18:48
will do this uh I keep things simple simple so this is the process
1:18:55
and um yeah so now what I want to do I'll clear this
1:19:02
and um I want you to uh groom all the
1:19:07
issues we have in our GitHub start with issue number for and uh if some things
1:19:13
are not clear, please use our plan.md document. It's located in the outdated
1:19:18
folder. But for now uh this is the what we used to uh seed our issues. So for
1:19:25
now for some of the assumptions you can check this file if you need but uh I think the issues should be
1:19:31
self-sufficient and um uh please do one issue at a time
1:19:38
for now. So I want to start with issue number four, right? So it will now uh
1:19:48
so now it should actually Yeah, you see it's it's reading the
1:19:54
instructions. It's reading this uh PM. So it knows what to do
1:19:59
because we described it. We described it in um our agents. We described that u
1:20:05
our work is organized. So it read this and it process. Okay, I did not describe
1:20:10
it. I should have actually like it's it's good that uh we did this because um
1:20:16
I need to also change the process that I didn't do roles.
1:20:24
Yeah. Um
1:20:30
cool. This is a part I forgot but good that the agent actually read it.
1:20:52
Uh quick question about Corsor. I we going to use Corsor. Uh Alio, you can
1:20:57
use whatever you want. You can use cursor, you can use codex, you can use clot code, you can use client, you can
1:21:03
use like whatever you want, right? So if you like courser, you can use cursor. I
1:21:09
don't use corser. I already have two subscriptions. I don't want to add another one on top of that. Um, so I
1:21:14
have codex and I have cloud code and for me this is enough. But cursor is good. I don't think it actually matters what you
1:21:20
use because they are more or less on the same level.
1:21:28
So um why is it creating issues? Ah okay. So a
1:21:34
follow-up issue that grooving number four required. Okay let's see
 Defining Checkable Acceptance Criteria
1:21:45
so it descoped some things. Um so I'll tell it uh please first update the issue and
1:21:54
then you create follow-up issues. Um so first I want to see the issue that is
1:21:59
clearly um that clearly follows um what we want right and then if something
1:22:05
according to the PM is out of the scope then we do this afterwards.
1:22:24
And then usually when I have to correct the agent when it's doing something uh what um what I also do is uh at the end
1:22:32
of the session this is what we will do right now together is I ask hey like based on um the corrections I made what
1:22:38
documents we need to update. So then the next time it doesn't uh it knows the uh
1:22:44
correct steps it knows the algorithm. Okay. So now it says it's uh groomed.
1:22:51
[snorts] So let's see. So the goal a visitor can create an account with a username, display name and password. Log
1:22:56
in, log out. No part of the flow touches email. There is no mail back end, no verification, no selfs serve password to
1:23:05
that. Okay. So then we have some acceptance criteria. Um so this acceptance criteria I see a
1:23:11
bit technical but um means that there is a page. So it renders a form uh username
1:23:18
uh already taken renders the form with a visible error. So this is very specific right? So it um we may agree with some
1:23:26
things, we may ask it to do some things but this is what we want to have right. So we want to have a very clear set of
1:23:33
acceptance criteria that we can uh the agent needs the agent knows what exactly
1:23:38
to implement. Uh and then we also have a way to test our application right because this acceptance criteria
1:23:44
criteria is what we are going to use later after this agent says it's done. Um we can actually test this uh test it
1:23:53
using the same criteria out of scope. So you see that it uh
1:23:59
figured out some things that are not in scope and things that are in scope and out of
1:24:06
scope. Um so like okay we don't need u brute force defenses.
1:24:13
Okay like I I wouldn't included this in the feature at all. It's kind of annoying that it always includes these
1:24:19
numbers, but okay.
1:24:27
Account settings changes play name.
1:24:33
Um for this uh let's uh make it uh priority
1:24:44
uh I don't know post MVP priority
1:24:50
at attack for that.
1:24:56
Um because I I think this could be useful but like I'm not sure how
1:25:02
useful it is for actually u maybe we don't even need this like it will create
1:25:08
some things that are out of scope but then we will also need to review them and say okay like this not really what
1:25:14
we needed.
1:25:20
So what I want you to do is just to have uh MVP and post MVP labels for the issues we created from uh 1 to 26 I
1:25:29
think mark them as MVP the rest should be post MVP. So whatever uh out of scope
1:25:35
issues PM uh I created right now they should be post MVP
1:25:43
and also based on uh my corrections based on what we uh did please find the
1:25:49
relevant documentation we have um and add some things to this documentation like um yeah like what you think uh
1:25:57
should be included there. first make a commit and then make changes.
1:26:03
So the reason I want to it to make a commit and then make changes is because I want to uh sometimes look at g and see
1:26:09
what exactly changed for code I don't um necessarily want to always do this uh
1:26:16
but for changes in documentation especially for changes in how um our
1:26:22
team works. So this is something I do um I want to see um because it influences
1:26:29
it affects the process right that's why I want to make sure that um we here
1:26:35
um we document it and I know what's happening here
1:26:41
okay so now we have this MVP label we have a
1:26:47
post MVP label
1:26:57
So demo data command. I think this is actually uh useful. So let's
1:27:05
MVP.
1:27:15
Okay. And now when these things are um saved I want to talk about loop
1:27:21
engineering. Even though loop engineering comes later here I think now this is the right time to introduce it.
1:27:27
So loop engineering is a way to
1:27:33
work through a pile of things you have uh or work on a specific thing. Right?
 Loop Engineering: Automated Multi-Task Goals
1:27:40
Right. So loop engineering um in principle is just this command you have in both codex and um clot. So they are
1:27:49
okay I have some here um some things. So prompt engineering this is what we say
1:27:54
to our coding agents. Context engineering is all the files that help our agent work like this is agent MD all
1:28:01
the processes all the things is context engineering and loop engineering is um
1:28:06
it right now we are driving the agents we are typing the prompts but prompt
1:28:12
engineering is going kind of one level more so it's more meta so we are we
1:28:18
engineering a prompt in such we engineer a loop in such a way that the loop is prompting our application our agent not
1:28:25
pass. So we say okay there are these issues. Now what I want let me take a
1:28:30
step back. What I want to do now is I want to uh for all these issues I want
1:28:35
to create uh I want to process them with a PM. Right? So then um for me what I
1:28:41
can do is I can just um set a goal. I can say go through all these things and
1:28:48
u create acceptance criteria for them and all the stuff we did right and if I
1:28:54
don't use the goal here um the agent can just stop after one or two issues right
1:29:00
so what I will do now is I'll say goal groom all the MVP issues
1:29:10
I think it asks some lens Um I can do four loose ends. Please make
1:29:20
clearly documented decisions. Right? Ideally you are more
1:29:25
involved in the process but also you want to review these files afterwards. Right? So now I set a goal and what will
1:29:32
it will do? it will uh go through all the MVP issues one by one and if at some
1:29:38
point um it stops the loop will prompt the agent
1:29:44
to continue right so it's not I will not need to babysit this agent and see okay
1:29:49
did it stop did it finish the task did it uh groom all the tasks because I have
1:29:55
this uh goal the goal will keep on uh
1:30:00
bugging the agent to keep on prompting in the agent to continue. Right? So this is the idea behind loop engineering.
1:30:07
There are two types of um loops in cloud code. One is goal.
1:30:13
This is what I use. Another one is loop. So loop is uh a scheduled prompt like
1:30:18
you can send a prompt like every 30 minutes saying hey how's how are you doing? Like are you done yet? Something
1:30:24
like this, right? And then cloud code can also stop the the loop. You can say you can instruct it. Um so there is a I
1:30:30
sent set a loop once the job is done please stop the loop right um
1:30:37
in case of codex you don't have loop you only have goals but this is something that you can actually implement yourself
1:30:43
if your agent doesn't support it uh you can use stop hooks and if you run it
1:30:48
your agent in a tumix session uh you can also send by through chrome you can send
1:30:54
some messages to this t-ox session uh regularly but like I use flat code I use
1:30:59
codex both of them support that I'm not sure about the others like corsor um I see a comment from Krishna loop
1:31:07
engineering is a pretty much hype in frontier labs is it used uh for day-to-day activities I use goal all the
1:31:15
time I use it very often I don't use loop often but goal is um this is
1:31:20
something I use very regularly okay so I changed a bit the order so I think I
1:31:25
will update this article and I put this um here after um
1:31:32
uh after grooming. But now let's see what is actually happening. So it's working and what I
1:31:38
can do in parallel is I can start another agent. So uh I need to go to TMP
1:31:47
and this is um how do we call it?
1:31:52
Oops. What's happening? It's AI dev tools experiments uh project
1:31:59
feedback. Then I start another team session and it will be what skill permissions. Okay. So I'm starting a new
1:32:06
session. So now I have this session. It's grooming this sessions.
1:32:12
So there are acceptance criteria and stuff. Um now what I want to do is for the issues that we groomed
1:32:19
like for example this one number four right? So I want to implement it. So for
1:32:25
that uh I want to create a software engineer. Right? So we have a product manager. Uh now I want to create a
1:32:33
software engineer. Software engineer will actually take this thing and it will implement them. So um let me see
1:32:43
here. So, I'm going to create a software engineer
 Creating the Software Engineer Persona
1:32:50
and I'm going to put this thing here,
1:32:58
right? Okay. Um, so now, um, I think I will
1:33:06
need to maybe restart the session. uh because I also want to no I will not
1:33:11
need to restart the session but I will need to update our process to also include
1:33:22
here. So this is something that agent uh added. I'll keep it makes sense. Um
1:33:29
so I need to add the engineer here. Right. And now uh in a fresh session
1:33:36
I'll say implement issue number four. Okay. So what I expected to do is to
1:33:41
discover that uh um there is this um
1:33:47
role software engineer.
1:33:53
So you see process. Yeah. So it found u the software engineer
1:33:59
role. Um yeah, I think I am a bit early for
1:34:04
that. Um maybe we will also need to implement
1:34:10
two and three or four.
1:34:16
Yeah, right. Cuz like uh none of the things that we need uh exist. Well, some
1:34:23
of them exist, but uh actually I don't think we can even run that.
1:34:34
Okay, I need to speed it up. So now it's
1:34:41
implementing uh 2, three and four. Uh then I will also need to have a QA
1:34:47
engineer a tester because we have this acceptance criteria, right? Um so we see
1:34:53
this acceptance criteria but the thing is engineers um usually what happens in
1:34:58
teams we have a special role for testing and often times if I wrote my code the
1:35:05
code myself um then um I am less critical of this code
1:35:12
right so usually you need a second pair of eyes to look at your code to review the code and u in companies where you
1:35:19
don't have you usually have uh some sort of like uh PR review uh code review like
1:35:26
these kind of things. Um so what we want to have is this sort of review and this
1:35:31
sort of testing right. We want something else not the engineer to review the work
1:35:37
of an engineer and we want this something QA engineer to say if actually
1:35:42
all acceptance criteria pass and then the verdict will be pass right or some
1:35:47
of them fail and then we will need to ask the certain engineer to implement the things right so we need a third role
1:35:55
the third role will be the QA engineer
 Quality Assurance and Graph Engineering Workflows
1:36:00
okay so we have team Q engineer. So this is the role the the
1:36:07
description um so here in description I say um how
1:36:13
exactly the QA engineer should behave and the important thing is it's always either pass or fail so it's always
1:36:19
binary true or false right um so yeah the the goal for the Q engineer
1:36:27
is to read the acceptance criteria and check each single one uh against the
1:36:35
uh test. Um I think we will need to update it. I'll ask maybe the next in
1:36:41
the different session to update it.
1:36:58
update for our project because we have npm here, right? So, npm
1:37:04
is u not really uh needed.
1:37:10
Okay. And this should be the quote. Okay. Um
1:37:18
so we have the Q engineer and we need to also add the Q engineer in the process
1:37:27
right so now we have these three roles we have PM we have engineer and we have QA right so PM grooms the task makes it
1:37:34
very concrete so we use this kind of specifications uh for making the task
1:37:40
complete concrete so the engineer doesn't need to um make a lot of decisions Then engineers implement the
1:37:46
groom tasks and QA checks the work of the engineer. And what it can do is it
1:37:52
can decide to whether the work is good and it passes the criteria or the work
1:37:59
is bad and the criteria are bad. Right? And what we happen when we put all these
1:38:05
three things together, all the three agents together is um what currently
1:38:10
people call graph engineering. If you open Twitter, you can see. So we have this graph. So this sequence of steps
1:38:16
that we have right so first we take a thing from the pool right our pool is um
1:38:25
uh this set of issues so we take one thing from this pool this is an issue and if this issue is not groomed yet we
1:38:31
groom it. So this is the first step in our uh pipeline right? So once it's groomed then an implement the engineer
1:38:38
takes this right. So the implementer takes this and uh works through this
1:38:44
then the next step is test. So we have this quality assurance and there are two
1:38:49
uh two possible outcomes. One outcome is pass then the task is done right. Another outcome uh is the task is not
1:38:58
done. It fails uh the verdict is fail. So then we um loop it back to the
1:39:03
implementer. The implementer needs to fix the task right and then um so this
1:39:09
is a graph right. So we have different responsibilities and the task goes through uh these responsibilities. So um
1:39:17
this is not new. the term appeared only like I don't know yesterday or when was it uh a couple of like I don't know
1:39:26
everyone on Twitter is talking about this but this is a pretty simple concept and um I have actually been using this
1:39:33
kind of thing for quite some time and uh there is uh this article
1:39:41
um I built an AI agent team for software development um you can check how I do do
1:39:48
this. So in in addition to PM software engineer and tester I also have a Q engineer you can check how I organize
1:39:54
the process. So here I just show you like a simplified version of that. Um
1:39:59
but um in this document there is a more um a version that I actually use right
1:40:04
so that the process that I have is a bit more uh complicated but you can check it but right now I want to actually
1:40:12
implement this graph. So I want to make sure that
1:40:18
um we can follow the steps and for that we need to have an orchestrator. So the orchestrator
1:40:24
is uh the main agent uh the main session of our agent that can start the PM that
1:40:32
can start the implement that can start the tester. So we don't have to do this ourselves right. So here I um have to go
1:40:40
here and type right here I also have to go here and type. So in a way for me
1:40:46
this orchestrator is both loop engineer and graph engineer right? So it knows
1:40:51
how to prompt these agents. So I don't need to pro to to prompt them myself and
1:40:56
it follows this process. It follows this graph right. So we need to um
1:41:02
to take this the rules uh process.
1:41:09
The main session is orchestrator. It launches the PM the engineer and QA as sub aents. it does not groom implement
1:41:14
or test itself. So typically previously when we were hey implement this task it would um start a it would do this within
1:41:23
the session. Now we say you need to launch a sub agent for that. So both codex and cloud code uh and also open
1:41:30
code and probably other uh engines can do that. They can launch sub aents.
1:41:36
Um okay life cycle uh and we basically describe the graph right. So we describe
1:41:43
the graph in simple terms in simple words uh one issues at a time. Um like I I
 Orchestrator Sub-Agent Execution and Wrap-Up
1:41:50
wouldn't necessarily enforce it. We can say um you can work uh on up to five
1:41:59
issues at the time. Yeah. Let's keep things simple. So in
1:42:04
reality I actually um work on oops I work on many issues at the same time
1:42:11
just to kept to keep things simple and see this um loop and this graph in
1:42:17
action we will actually uh now do this. Okay so let me see um so it updated the
1:42:24
key engineer so let clear it uh it is still implementing these
1:42:30
things. Okay. So it's going through issues from one to
1:42:37
four but I think so issues one to three um
1:42:42
they are fairly technical. The first real user issue start with number four.
1:42:48
So I think this for us is the interesting issue to actually um use this approach use this framework. So for
1:42:55
these ones uh they are more like um yeah they they just need to I would not use
1:43:01
any fancy process for them. I just would get them done
1:43:09
docker compos environment.
1:43:14
Okay. Okay. So it probably mentioned them because uh there is dependency on that right
1:43:25
out of scope. Okay, whatever. Um so where are we?
1:43:32
So I kind of wanted to show you the actual loop. So let me let's wait till it finishes.
1:43:39
Um yeah. So graph is basically a workflow. Yes.
1:43:45
How did you write this? Uh what do you mean? Um how did I write what? How did I
1:43:50
write uh this um these things? So for me this is based on I've been using agents
1:43:58
for quite some time. So this is the process I follow when working on my own uh projects. And what I show here in
1:44:06
this session is more like a distillation of this. Right? So if you take a real project that I have, let's say um AI
1:44:15
shipping locks, right? So I I think I should go to GitHub.
1:44:22
So the process there is more complicated, but the idea there is kind
1:44:28
of similar, right? So you have this process.md document that describes the process. Um
1:44:34
so the graph here that we have is a bit uh more complicated, right? Uh but uh so
1:44:40
what I did here is I took all of this from many different projects where I use
1:44:47
uh this approach and I kind of condense it into something right and at the
1:44:52
beginning you need to start simple right and then the file will grow itself
1:44:58
because at the be at the end after each session you can say hey like what do we need to improve in the process or when
1:45:03
you see that you need to steer the agent manually. So you ask it hey like can you
1:45:09
please update our process so I don't need to do this right? So for example I say which kind of models it needs to use
1:45:15
for the agents right and then because I use uh often I use clot and codex at the
1:45:21
same time. So I have the the agents that are um defined in the clot format but
1:45:27
then I also describe for codex how to actually um run these agents.
1:45:34
So this is how these things appeared. Okay. I do are we down here?
1:45:40
Uh but anyway, so uh now if I want to show
1:45:48
you this uh graph engineering, this would be it. So I write a goal and write
1:45:53
work through the back block, right? So now this would
1:46:02
uh maybe I need to focus on MVP
1:46:10
issues only. Right. Um
1:46:17
okay. So I'll let it finish and then I run this. Um
1:46:25
yeah because I want to show you how exactly it looks like how it starts ovations and stuff.
1:46:33
Um, let's stop. Which issue are you
1:46:40
working on?
1:46:47
Okay. Um close uh the done issues
1:46:54
and create a
1:46:59
note to
1:47:04
issue number four about what what you have done so far.
1:47:13
Okay. Okay. So I want to just take this and run this as a separate session.
1:47:37
Okay. Smart software engineer. The engineer doesn't close issues. K check some you're already that okay
1:47:52
so I just do this then I start with or
1:47:58
see comments
1:48:08
okay so let's see the first. So this agent is the orchestrator, right? So we see that
1:48:15
goal is active. So it will figure out the current state
1:48:20
and uh it will see what is happening there. Right? The issue is already
1:48:26
groomed has a be work in progress comments. Um
1:48:33
so then it says handing number four to the engineer. You see now we have this
1:48:38
thing here. So there is actually an agent a sub agent that started it. So
1:48:45
because I did not follow the convention for defining agents that is in clot
1:48:52
that's why it just calls it clo right. So if I want to have proper names here if I want to see that this is actually a
1:48:58
software engineer so then I would need to do something like
1:49:03
here go to clot create agents and then put them here. I want to make it um
1:49:11
engine agnostic that's why I want it to work with any coding agent that supports
1:49:16
sub agents and this approach will work right um so it will work in codex it
1:49:21
will work in open code I don't know if if cursor supports sub aents if it does
1:49:26
it should also work there right so and this is it um what I will do is it will
1:49:33
probably take a few hours to actually go through this spec lock and implement all the things so what I will do is I will
1:49:40
put all the code online and I will refer it and you can also look at the issues.
1:49:46
Um I can also include a few issues from AI shipping labs so you see how I use it
1:49:51
on real projects. Okay. Um do you have any questions? Um I
1:49:57
know we took a bit more time. Uh yeah so it wasn't uh 90 minutes it was more but
1:50:02
I think I covered everything. So um please subscribe to Substack. So, I will
1:50:08
be putting more content here. Click on this button.
1:50:14
I will putting more content here. So, I'll put the next three uh lessons here
1:50:20
too. Um so, yeah, if you want to keep um
1:50:26
um if you want to get notifications about this, so please subscribe and I will of course also based on what
1:50:33
we did today, I am going to update it. I'm going to add some pictures. In fact, I published this like 2 minutes before
1:50:40
we started. So, I will need to to update it because it was like a bit rogue kind of.
1:50:46
Okay. Um well, that's it for today. Um
1:50:52
yeah, I see some questions. So, per personal project. This is how it's done. Uh working with Markdown files. Yes. So,
1:50:58
this is how I do it for my personal projects. Well, for me, um,
1:51:03
I have both projects that I work on professionally and projects that I work on personally. And all of these projects
1:51:10
kind of follow a very similar structure, right? So, I describe uh this thing that
1:51:16
the link is at the end. Um, so this is more or less the process
1:51:22
I use for all my coding projects, right? And uh when I start a new one, what I do
1:51:28
is I say uh hey like there is a process that I use in this and this project but
1:51:34
in this project the new project that I'm starting I use this and this technologies. So please take the process from there adjust it to new technologies
1:51:42
and then commit. So this is going to be my first like commit uh in uh in a new
1:51:47
project right even before I bootstrap the project. Of course like I also include plan I
1:51:54
also include the architecture decision and then when it's there then I bootstrap the process and then I start
1:52:00
working on the issues and then typically the first few issues as you see they are
1:52:05
more technical so for that I don't need to follow the process but once we start talking about um userf facing things so
1:52:12
then I want to follow the process I want to have like always have a QA always have a product manager not just the the
1:52:19
implementer for some things I use this. So for example, for these courses, I started this project long time ago and
1:52:27
um so here I don't really follow the process. Um
1:52:33
but yeah, so there I need to be a bit more careful with tests and stuff, right? Because in practice I see that um
1:52:41
following this process, especially the tester part really helps. The tester often finds some things that a software
1:52:48
engineer missed. So this is quite important.
1:52:53
Um one note though that if you follow the process you will consume a lot more
1:52:58
tokens right because now in uh um in addition to just implementing this thing
1:53:04
you have all the other things right and then uh naturally your token consumption goes like I don't know four five times
1:53:11
more for each single issue because you need to groom it you need to implement it you need to test often times tester
1:53:17
decides to uh fail to say that uh this is failing. So then you need to go back,
1:53:24
you need to implement this. Uh but what you get in return is uh better quality.
1:53:30
Okay, I don't see any other questions. Um so I think I should um stop here. Um so
1:53:39
thanks a lot. The article will be updated so keep an eye on it and um yeah
1:53:45
see you soon and we will have another session like that in a couple of weeks. I don't remember when exactly. Think I
1:53:52
can check. Uh I think you can find it if you go to
1:53:58
our LM Zoom camp and there is a list here.
1:54:06
Where is it? Oh, wrong link. Sorry. AI dev tools
1:54:13
here. Workshop number two SVP. And it happens in um what
1:54:23
it's in August, so in a couple of weeks. So yeah, that's it. Um thanks a lot and
1:54:31

https://aishippingblog.com/p/ai-native-development-specifications
https://aishippingblog.com/p/ai-native-development-specifications


Alexey On Data
Alexey On Data


AI-Native Development: Specifications, Loop and Graph Engineering
Part 1 of the AI Dev Tools Zoomcamp series
ALEXEY GRIGOREV
JUL 22, 2026

This is the first article in a series based on AI Dev Tools Zoomcamp, the free course we run at DataTalks.Club.

Part 1: AI-Native Development: Specifications, Loop and Graph Engineering (this article)
Part 2: Build and Ship a Full-Stack App with AI Coding Assistants
Part 3: Deploy a Full-Stack App with AI Coding Assistants
Part 4: DevOps and Observability for an AI-Built App
Part 5: TBA
I start with AI-native developer workflows. We will see how to turn a raw idea into a specification, give coding agents the right context, and verify what they build.

Subscribe to receive the next article in the series.

Subscribe

Coding agents now write code faster than I can read it.

When we give an agent a task, it can quickly implement it. But if a task is vague, the agent fills the gaps with its own assumptions. A weak agent that misunderstands us writes fifty lines of broken code. A strong agent that misunderstands us creates eight files, wires them together, and adds tests that pass. The code works, but it isn’t what we needed.

We no longer spend most of our time typing. We spend it saying precisely what we want and checking what came back.

In this article, I show how to make the request specific so the agents don’t need to guess. Then we decompose the request into tasks and assign them to a product manager, a software engineer, and a QA engineer. Finally, we implement all the tasks in a backlog through a loop.

We cover topics like:

Spec-driven development
Context engineering
Loop engineering
Graph engineering
We’ll use a deliberately vague project idea: a tool for weekly feedback for projects. It doesn’t say who gives the feedback, who receives it, or what “projects” means.

You can see the final result in the retroloop repository.

Specs before code

We need to understand what we want to build before the agent produces the first line of code. We have to think it through in detail and give explicit instructions. If we do that, the agent will produce something close to what we want.

We call this “spec-driven development”. We start with the specification, make sure it aligns with our vision, and only then write the code from it.

In our example, “a tool for weekly feedback for projects”, many things aren’t clear.

Who are the users for this tool?
What problem will they solve?
How are they going to use it?
If we don’t specify these things and give the idea directly to a coding agent, it’ll fill the gaps.

When I asked Claude Code to implement this project, the only prompt I gave was “a tool for weekly feedback for projects”. It came up with weekly-feedback, a command-line tool for tracking weekly project status. It records wins, issues, blockers, and next steps. It also created documentation and covered the app with 62 tests, all of which passed.

The one-shot weekly-feedback CLI


It all works perfectly, but that’s far from what I needed. I needed a web tool for a team retrospective that captures feedback from teams in the form of “Start/Stop/Continue”. It was my fault for not telling Claude that.

Start in a chat assistant

Instead of giving a prompt directly to the coding assistant, I start in a chat application and talk the idea through. I use ChatGPT in dictation mode for this.

I begin with the same vague idea:

I want to build a tool for weekly feedback for projects.

Help me set the scope for this project precisely. I want to brainstorm with you
and understand how the tool should work. Give me options.

Ask me one question at a time and keep your output short.
This way, we can use AI as our brainstorming partner and find out precisely what we want:

Who contributes feedback? All team members.
What format do they use? Start/Stop/Continue.
Is the feedback anonymous? Names appear by default, but contributors can choose to remain anonymous.
What can people see before the reveal? Only their own cards.
How does the facilitator reveal the feedback? All cards appear at the same time.
What happens next? The team clusters the cards, then each person casts three votes for the topics to discuss and can give multiple votes to one topic.
What does the team record? Decisions and action items from the discussion.
Can the facilitator add a recording? They can upload audio, video, or a transcript after the meeting, but built-in recording isn’t part of the first version.
When we finish, I ask for a file with all the specifications:

Save everything to a markdown file that I can download.
Download the file and save it as plan.md.

Bootstrapping a project

Create a project from this specification:

mkdir project-name
cd project-name

git init
Copy the plan.md file:

mkdir -p _docs
mv ~/Downloads/plan.md _docs/plan.md
git add _docs/plan.md
git commit -m “Add project plan”
You can find the plan.md file from this project in the Retroloop repository.

I try to commit as often as possible, after every meaningful decision. With those commits, we can review what the agent changed. If something isn’t working well, we can easily return to the last good state.

Choose the stack and architecture

During the brainstorming session, we didn’t choose the tech stack.

Ask the coding agent to come up with several options:

Read _docs/plan.md. Propose multiple options for the tech stack and
explain each option.

Don't write code yet.
It proposes multiple options and explains the tradeoffs of each one.

I choose Django because I know it well enough to review. In your case, you can select any technology you’re comfortable with. It’s also okay not to have a preference and to let the agent select what it thinks will work best.

Turn the decisions into a backlog

Now that we’ve settled on the tech stack, we can ask the agent to decompose the specifications into a backlog with tasks:

Create a backlog with tasks in _docs/tasks.md.

Each task should be small enough to finish in one session, and
independent enough that I could hand it to someone who has not read
the others.

Use this template for each task:

## <number>. <title>
Goal: <one line>
Description: <two or three sentences on what the task involves>

The first task should be setting up an empty project with a passing test.

Don't write code yet.
It created these tasks.md.

Review the tasks and ask the agent to merge tasks that are too small or split tasks that don’t fit into one session. We want to create an MVP - the first version of the app. If something is out of scope for your vision of the MVP, remove it.

When we’re happy with the tasks, move them to a task tracker. I use GitHub issues for that.

Ask the agent to do it:

Create a public GitHub repo for this project.
Move each task from _docs/tasks.md into a GitHub issue.
For that to work, we need the gh CLI tool authenticated and the repo connected to the GitHub remote.

From this point on, GitHub issues are the canonical tasks and the only active backlog. We no longer need _docs/tasks.md.

Context engineering

The repository has a backlog now. When we start a new session, however, the agent doesn’t know which task we mean. It must figure that out every time.

These details go in AGENTS.md, which coding agents like Codex or OpenCode read when they start a new session.

Claude Code reads CLAUDE.md, while I use multiple coding assistants and want my workflow to be tool-agnostic.

That’s why I also create CLAUDE.md with a single line:

@AGENTS.md
It tells Claude to read AGENTS.md.

This is called context engineering. With prompt engineering, we control one message in one session. With context engineering, we control what agents know when they start a new session and what information they can find while they work. We include useful facts and working rules they would otherwise have to rediscover.

AGENTS.md

To make this context available in every new session, create AGENTS.md:

Commands

- `uv sync` - install dependencies
- `uv run pytest` - the whole suite
- `uv run pytest tests/test_home.py` - one test file

Rules

- Dependencies are added in `pyproject.toml`. Do not add one without
  asking
The other documents

In addition to AGENTS.md, I usually have a few other Markdown documents in my projects.

The main one is process.md, which I use to describe how work is organized. It could live inside AGENTS.md, but I keep it separate.

Create _docs/process.md:

- Tasks are GitHub issues, one at a time
- Read the acceptance criteria before starting and before closing
- Commit regularly
As I continue working on a project, I may create other documents, such as:

testing-guidelines.md for testing
design-system.md so the UI doesn’t drift every session
api.md, which describes what the API should look like
I keep them together in _docs/ and link them from AGENTS.md:

Documents

- `_docs/process.md` - how work is organized
- Before writing tests, read `_docs/testing-guidelines.md`
- For anything touching the UI, read `_docs/design-system.md`
The agent reads AGENTS.md at the start of every session, so it knows where to find the process, testing, and design rules if it needs them.

This way, it will load the design system only for a UI task and the testing guidelines only for a testing task. By loading each document only when it’s relevant, we keep AGENTS.md short while we continue adding written context to the project.

These documents are living documents, and I update them often. If I need to correct an agent during a coding session, I can ask it to modify the documents. Next time, it knows what I need, so I don’t have to correct it again.

You can use a prompt like this:

Based on the corrections I made, find the relevant documents and update them.
Commit the current work before changing the documents.
This is the first article in a new series based on AI Dev Tools Zoomcamp, the free course we run at DataTalks.Club.
This year, I’m publishing the course notes as standalone articles, with one article for each module. Subscribe to receive the next article in the series.

Subscribe
Bootstrap the first task

With AGENTS.md and process.md in place, we can start a new session and ask the agent to implement the first task:

Implement task 1.
For this project, the agent creates the Django app, dependencies, and a passing test.

Grooming: the product manager agent

We have a backlog of tasks, but they’re not precise enough.

We discussed this problem already: if the task isn’t specific, the agent will fill in the gaps during implementation. We risk spending time and tokens on something we don’t need.

Instead, we should ask the AI assistant to fill these gaps before writing any code. Then we review the specification, correct it, and give it to the coding agent to implement.

This process is called “grooming”: we groom a task to make it more specific. Then an engineer can implement it without asking a single question.

In real teams, product managers usually do this work. Here we’ll create a team of agents, and the first role we’ll define will be a PM.

Create a document:

_docs/team/
  pm.md
Inside, write the description for the product manager agent:

You’re a Product Manager

You groom a task before anyone implements it.

- Read the issue as written
- Rewrite it using the template in `_docs/task-template.md`
- Make the acceptance criteria checkable - someone should be able to
  point at the screen and say yes or no
- Think about the edge cases the person who filed it did not consider
- Do not write any code

Definition of done:

- The issue has all four sections filled in
- Every acceptance criterion can be checked by looking at the result
- Everything moved out of scope links to a follow-up issue
- An engineer who has never spoken to you could implement it from the
  issue and the documents it links

If something does not belong in this task, do not silently drop it.
File a follow-up issue and list it under out of scope with a link to
that issue, so it is clear what was moved and where it went.
A groomed task has four sections:

Goal - one or two sentences on what should be true afterwards.
Acceptance criteria - checkable statements.
Out of scope - what this change must not do.
Constraints - files it should stay inside, libraries it should or shouldn’t use, prior decisions it has to follow.
We save the issue template as _docs/task-template.md:

## Goal

One or two sentences on what should be true when this is done.

## Acceptance criteria

- [ ] A statement you can check by looking at the result
- [ ] One line per case, including the awkward ones

## Out of scope

- Something that does not belong in this task, moved to #TASK-NUMBER

## Constraints

- Files this should stay inside
- Libraries to use
- Guidelines to follow
We’ll need to groom every task, so we’ll add it to process.md:

Roles

- PM - grooms a task before anyone implements it, follows _docs/team/pm.md
We can now start a new session and ask the agent to groom an issue:

Groom issue #4
After it finishes, review the result.

We can catch a misunderstanding most cheaply while grooming: the issue is a paragraph, and correcting it costs one sentence. If we catch the same misunderstanding after implementation, we need a rewrite.

Loop engineering

After grooming one issue, we can ask the agent to groom the rest:

Groom all GitHub issues. Process one issue at a time.
This will mostly work, but the agent may eventually stop. It might say, “I’ve groomed issues 1, 2, and 3. Do you want me to proceed?”

The answer is almost always “yes”, but the agent has stopped and is waiting for us to say that explicitly. In many cases, I want the agent to continue automatically.

To do it, we can give the agent a goal:

/goal groom all issues
The /goal command will prompt the agent to continue, so we won’t need to do it manually. Instead, we delegate that responsibility to the harness: the system around an agent, such as Claude Code or Codex. When the agent stops, the harness checks whether the condition has been met. If it hasn’t, the harness resumes the work.

The goal prompts the agent to continue


This approach is called “loop engineering”. It’s similar to a while loop: we repeat the work until a condition is met.

With loop engineering, the system runs a coding agent repeatedly instead of having us drive it manually, prompt by prompt.

There are multiple “engineering” levels when we work with coding agents:

Prompt engineering - what we say when we interact with the agent
Context engineering - what the agent knows before it starts and what it can get during the session
Loop engineering - when it stops working
Graph engineering - who does what when there’s more than one agent (we’ll discuss it later)
In June 2026, Addy Osmani published the Loop Engineering essay that gave it a name, and Peter Steinberger compressed the idea into one tweet:

Peter Steinberger 🦞
@steipete
Here’s your monthly reminder that you shouldn’t be prompting coding agents anymore.  You should be designing loops that prompt your agents.
7:58 PM · Jun 7, 2026 · 8.49M Views
1.8K Replies · 1.41K Reposts · 19.9K Likes
A loop needs a stop condition: a checkable statement that tells the harness when to stop.

For /goal groom all issues, the stop condition is “all issues are groomed”. After each agent run, the harness checks whether that condition is true and resumes the agent if it isn’t.

The stop condition must be something the model can evaluate. “All issues are groomed”, “all tests pass”, and “no file is over 200 lines” are checkable, but “make the code better” isn’t. If the stop condition isn’t checkable, the agent can stop too early or run forever.

Claude Code and Codex provide the /goal loop by default. If your harness doesn’t provide it, you can implement it yourself using stop hooks.

Implementation: the software engineer agent

After grooming the issue, we can give it to a software engineer, the agent who will write the code.

Define the second role:

_docs/team/
  software-engineer.md
Put this definition inside:

You’re a Software Engineer

You implement one groomed task at a time.

- Read the issue and implement what it describes
- Implement against the acceptance criteria, do not change them
- Stay inside the files and constraints the issue names
- Write tests for what you built
- Do not close the issue
- Commit regularly

Definition of done:

- Every acceptance criterion in the issue is implemented
- Tests are written for the new behaviour, and the whole suite passes
- The work is committed
- The issue is still open, with a comment saying what you did

If an acceptance criterion is wrong, impossible, or contradicts
another one, create a comment on the issue about it.
Add one more line to process.md:

Roles

- PM - grooms a task before anyone implements it, follows _docs/team/pm.md
- Engineer - implements one groomed task, follows _docs/team/software-engineer.md
Then ask the agent to implement a task in a fresh session:

Implement issue #2
The engineer stops when the code is written and its own tests pass. It’s still too early to say that the task is properly implemented, so we need to test it.

Testing: the QA engineer agent

When the same agent writes and judges the code, it’s grading its own homework.

If we ask, “Is this correct?” we’ll get a definite “yes”, but the agent might have missed many edge cases.

In the real world, we ask other people to validate our work. We have code reviews, and many teams have designated QA engineers whose focus is making sure the code is reliable.

That’s why we’ll also add a QA engineer to our team.

Add the third role:

_docs/team/
  qa-engineer.md
The description:

You’re a QA Engineer

You check finished work against the issue that specified it.

- Read the acceptance criteria from the issue
- Check each one against what the code actually does
- Run the tests, and say which ones you ran
- Look for the cases the criteria describe but the tests do not cover
- Do not fix anything you find. Report it by creating a comment

Your output is a verdict: PASS or FAIL. It is FAIL if a single
acceptance criterion fails. Post it as a comment on the issue:

## QA: FAIL

- [x] A visitor can create an account with a username and password - PASS
- [ ] A duplicate username shows a visible error - FAIL
      Submitted an existing username and received an unhandled error

Tests: `uv run pytest`, 18 passed, 0 failed

Definition of done:

- The comment starts with PASS or FAIL
- Every acceptance criterion has a verdict against it
- Every FAIL says what you did and what happened
- The test command and its result are included
- Nothing in the code was changed

Ignore what the implementation says it does. Only the acceptance
criteria and the running code count.
Note: you may need to adjust this role for your project if you don’t use uv and pytest.

And the last line in process.md:

Roles

- PM - grooms a task before anyone implements it, follows _docs/team/pm.md
- Engineer - implements one groomed task, follows _docs/team/software-engineer.md
- QA - checks the result against the acceptance criteria, follows _docs/team/qa-engineer.md
Then, in a new session, ask:

Test issue #2
If we get a PASS, that’s great. If we get a FAIL, that’s also useful: we caught a regression. So we start a new engineer session, use the QA comment as input, and ask the engineer to fix it.

We iterate until QA says PASS.

Graph engineering

We have three roles:

Product manager grooms an issue
Software engineer implements it
QA engineer tests it, outputs PASS or FAIL
If QA says FAIL, the engineer will need to reimplement it. Otherwise, the task is done.

We can visualize this process as a graph:

01-agent-workflow-styled.png
If we have an orchestrator that launches these agents automatically instead of us doing it manually, we get “graph engineering”. We define a graph with specialized agents as nodes and describe how the work moves from one to another.

The earliest explicit use of the term I found in the article from Josh C. Simmons (July 4, 2026): The Graph Engineering phase.

Peter Steinberger sparked a wider discussion in a July 18 post by asking whether the conversation had shifted from loops to graphs. A few hours later, Hamel Husain used “graph engineering” in an article headline.




Hamel put just a GIF saying “stop it” in the article, but people liked the term and started using it for multi-agent orchestration.

I wouldn’t call it a new idea, though, and loop engineering is definitely not dead. Even with graphs, we still need a loop to drive the work and orchestrate it across multiple agents with different roles.

The orchestrator

To implement it, we need an orchestrator.

Describe it in process.md:

Orchestrator

The main session is the orchestrator. It launches the PM, the engineer
and QA as subagents. It does not groom, implement or test itself.

Lifecycle

1. Pick the next open issue from the backlog
2. PM grooms it
3. Engineer implements it
4. QA verifies it
5. On FAIL, back to step 3 with the QA comment as input
6. On PASS, close the issue
7. Repeat until the backlog is empty

Rules

- Do not skip step 2
- The engineer does not close the issue
- QA does not fix the code, only outputs PASS or FAIL
- The orchestrator closes the issue only after QA outputs PASS
We can now start a fresh session and launch the loop:

/goal work through the backlog
The agent reads AGENTS.md, finds process.md, follows the lifecycle, and dispatches the agents according to the documents in _docs/team/.

Because we combine it with a goal, the orchestrator runs until the condition holds.

You can see the result in retroloop.

Note: this approach takes significantly more time and tokens than a direct loop with only a software engineer. In many cases, you don’t need this complexity. Often, a simple prompt or loop is enough.

I’ve followed this approach on many projects, including the AI Shipping Labs website.

I describe it in I Built an AI Agent Team for Software Development. Here, I distill that article into a tutorial.

Next in the series

We have now finished the first module. It’s theoretical, but the next modules are very practical.

We will implement an application from the specification to making it production-ready in 3 steps:

Build: Build and Ship a Full-Stack App with AI Coding Assistants
Deploy: Deploy a Full-Stack App with AI Coding Assistants
Operate: DevOps and Observability for an AI-Built App
Subscribe to receive the next article in the series.

Subscribe
94 Likes
∙
10 Restacks
Discussion about this post

Lious
16 Aug

Your point that a strong agent can build the wrong thing more efficiently is exactly why I see specifications as context infrastructure, not preamble. One extension I would add is provenance: every acceptance criterion should retain the decision, source, or user signal that created it. That gives the PM agent something to challenge, the engineer a boundary to respect, and QA a reason behind the check. Otherwise a well-groomed issue can still preserve a stale assumption with impressive precision. The graph becomes much safer when its handoffs carry both requirements and their evidence.
LIKE (2)
REPLY
SHARE
Marco
5d

This was really cool, thank you! As someone who worked as a software engineer before, it's incredible how fast you can get a project set up with this AI-native workflow. I can also see it removing many of the long grooming meetings with the product team.
LIKE
REPLY
SHARE
1 more comment...

How I Dropped Our Production Database and Now Pay 10% More for AWS
A Terraform command executed by an AI agent wiped the production infrastructure behind the DataTalks.Club course platform. Here’s how it happened and…
MAR 6 • ALEXEY GRIGOREV

168

34

12


I Built an AI Agent Team for Software Development and Tested on 5 Real Projects
I assigned agents to PM, SWE, QA, and on-call roles and used the setup across five different software projects.
APR 3 • ALEXEY GRIGOREV

37

6

5


What AI Forward-Deployed Engineers Do
An Analysis of 113 AI FDE Job Postings
JUL 25 • ALEXEY GRIGOREV

72

3

6


Ready for more?

Subscribe
© 2026 Alexey Grigorev · Privacy ∙ Terms ∙ Collection notice
Start your Substack
Get the app
Substack is the home for great culture
