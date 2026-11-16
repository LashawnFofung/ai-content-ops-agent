---
name: "career-pivot-episode"
description: "Produce and publish a Career Pivot episode end to end: interview, script, voiceover, long-form + 2 Shorts, thumbnails, community posts, then package for Substack, Spotify, Apple Podcasts and LinkedIn with cross-links."
---

# Career Pivot Episode Agent

Runs one episode of Lashawn Fofung's **Career Pivot** series (healthcare → tech → product) from topic to cross-linked release. Trigger: "Run Career Pivot Ep. N" (or "next Career Pivot episode"). The series order so far: Ep. 1 Clinical Informatics, Ep. 2 First Tech Role, Ep. 3 Scrum Master + MBA, Ep. 4 Earning my PMP (next).

Work in stages. Each stage ends at a **gate**: show the output, wait for Lashawn's OK, then continue. Never publish, post, send or schedule anything without her explicit yes for that item.

## Sources of truth (read first)

- Brand & Content Plan (doc) — series names, title format, schedule, guardrails
- YouTube Digital Assets Record (sheet) — "Ready to upload" and "Published videos" tabs
- Brand assets (design system) — LF monogram, avatars, show art, colors
- Previous episode doc ("Career Pivot Ep. N-1: …") — copy its structure exactly

## Guardrails (always)

- Keep the current employer vague: no employer name, internal numbers or projects in public content. Say "healthcare technology" or "my current role."
- No patient details. Say "insurance plans," not "Medicare."
- Her real words come from the interview; never invent facts, dates or numbers. Mark gaps as open questions.
- Motto closes every episode: "Don't just do it. Learn it. Apply it. Grow it. Repeat."

## Stage 1 — Episode doc + interview

1. Create the episode doc "Career Pivot Ep. N: <topic>" (Docs type), same sections as the previous episode: Explainer, Interview notes, Scene plan, Read-aloud script, Recording checklist, Publishing kit.
2. Write a short plain-language explainer of the topic (what it is, how it works).
3. Interview Lashawn: 5 questions, one at a time or as a list she answers by voice: why this step, how she did it, what it took (time, cost, study), a story, one lesson. Log answers in her words.

**Gate 1:** interview notes approved.

## Stage 2 — Script and scene plan

Skeleton framework, about 4:30–6:00:
1. Hook (under 30 s): proof line + one promise.
2. Series open: "Welcome back to Career Pivot… last episode … this time, I'm taking you back to <year>."
3–7. Five points, each: hook, explanation, story, wrap-up.
8. Close: why it matters, one action this week, motto, next-episode tease, subscribe.

Add (pause) marks. Scene plan table: #, scene, on-screen visual, voiceover part. Recording checklist: one Voice Memo per numbered part, say the part title first.

**Gate 2:** script approved. Lashawn records and uploads the voice files.

## Stage 3 — Voiceover mastering

- Cut the spoken slate before the first pause ≥ 0.85 s; tighten long pauses.
- Chain: high-pass, afftdn, EQ, de-esser, compressor, two-pass loudnorm to −16 LUFS.
- Word-align to the script (pocketsphinx) for scene timing.
- Fix any value she corrects (dollar amounts, dates) in on-screen text, not by editing her voice.

## Stage 4 — Video build

- Long-form: 1920×1080, 30 fps, Career Pivot look (LF badge, "CAREER PIVOT · EP. N" pill, illustrated avatar, timeline highlighting the year). Original music bed with sidechain ducking under VO. Master −14 LUFS, −1 dBTP. Concat with setpts=N/30/TB.
- 2 Shorts: 1080×1920, 30–45 s, each one point from the episode (a framework or a story), captions burned in, end card "Full episode: Career Pivot Ep. N".
- File names: Career_Pivot_EpN_<Slug>.mp4, Career_Pivot_EpN_Short_1.mp4, Career_Pivot_EpN_Short_2.mp4.

**Gate 3:** Lashawn reviews renders.

## Stage 5 — Thumbnails and images

- YouTube thumbnail 1280×720 (main) + a second variant for Test & Compare.
- Short covers 1080×1920.
- Community post image 1080×1080 (YouTube crops posts square).
- Substack header for the top of the post: 16:9, 1456×816 (LF badge, "CAREER PIVOT · PODCAST EP. N" pill, waveform, avatar on mint rings, episode title). Never use a 1.91:1 image as the post cover; Substack crops it.
- Substack social preview: 1220×630, set in the post's Settings → Social preview image. Same design reflowed for the wide frame: title on the left, avatar on the right, all text inside the frame and clear of the rings. Also save a 1200×630 copy for other link previews.
- Square social image 1080×1080 for LinkedIn feed posts.
- Podcast episode art: reuse the Career Pivot show art (podcast_art_url from the previous episode).
- Add finished covers to the brand assets Covers group.

## Stage 6 — Publishing kit (in the episode doc)

- YouTube title: "Career Pivot — Ep. N: <Outcome title>" (series first). Shorts: hook-first title + #shorts.
- Description: first line "Full write-ups and my work: https://lashawnfofung.substack.com/p/start-here", hook, what you'll learn (5 lessons), action, previous-episode link, chapters (from aligned timings), next-episode tease, motto, 5 hashtags.
- Shorts descriptions: one line + "Full episode: <long-form link>" + hashtags; set Related video to the long-form.
- Community posts: launch post (day of) and a poll (2 days later; text only, 4 options).
- Schedule: long-form goes live at 12:00 PM or 7:00 PM ET, never 12:00 AM. Through Dec 14, 2026, use the slot in the Brand & Content Plan's go-live time test; after the Dec 21 analytics review, use the winning time. Post on LinkedIn only outside work hours: within an hour of a 7:00 PM go-live, or at 5:15 PM ET for a 12:00 PM go-live; never schedule LinkedIn posts during the workday. Shorts on later days in the week after; add all rows to the assets record "Ready to upload" tab.

**Gate 4:** Lashawn uploads to YouTube and sends the video link.

## Stage 7 — Package from YouTube to other platforms

1. **Substack (feeds Spotify + Apple Podcasts):** create a draft via the Substack API in the browser: type "podcast", draft_section_id = the Career Pivot section ID, season "1", episode "N", podcast_episode_type "full", podcast_art_url = show art, title "Career Pivot Ep. N: …", subtitle under 120 characters. Body like Ep. 2/3: hook, "In this episode" bullets, bridge paragraph, action, motto, next episode, ▶ YouTube link, ⏮ previous episode, Episode notes, comment prompt. Lashawn uploads the .mp4 in the editor (Substack extracts the audio for the RSS feed) adds the 16:9 header image at the top of the post, and sets the 1220×630 social preview image in Settings → Social preview before publishing. Ask whether to email subscribers before publishing.
2. **Spotify and Apple Podcasts:** distributed by the Substack podcast RSS feed; verify the episode appears within a day. Provide a 600-character episode description in case a platform needs it.
3. **LinkedIn:** a post in her best-performing format (one-line hook, the result, then how), green/orange image, link in the first comment, no current-employer specifics. Optionally a carousel of the 5 lessons.

**Gate 5:** each post approved before it goes live.

## Stage 8 — Cross-link and log

- YouTube long-form description: add the Substack post link; add "Up next: Ep. N" to the previous episode's description.
- Shorts: Related video = long-form; add all three to the Career Pivot playlist.
- Substack: link the YouTube video and the previous episode; update Start Here if the series list is shown there.
- GitHub: only when the episode covers a build, link the repo in the description and add the video/post links to the repo README.
- Assets record: move rows from "Ready to upload" to "Published videos" with markdown links and IDs.
- Brand & Content Plan: tick the episode in Next up and add the next episode.

## Done = all of these

Long-form + 2 Shorts live and in the playlist · thumbnails set · launch post + poll scheduled · Substack podcast post published · episode visible on Spotify and Apple · LinkedIn post live · every platform links to the others · assets record and content plan updated.
