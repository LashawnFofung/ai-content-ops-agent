# AI Content Ops Agent

**One voice recording becomes a long-form video, 2 Shorts, a podcast episode and social posts across 6 platforms, with a human approving every publishing step.**

I'm Lashawn Fofung, a clinician turned Technical PM and AI builder. I run my personal brand like a product. This repo documents the agent system that produces and distributes my **Career Pivot** series: what it does, how it's designed, and where AI acts versus where I decide.

> Built with Claude (Anthropic) as the agent, Python and ffmpeg for audio and video, and the Substack, YouTube and LinkedIn platforms for distribution. I design, decide and approve; the agent drafts and builds.

## See it live

- YouTube: [Career Pivot Ep. 3: From Nurse to Scrum Master](https://youtu.be/-xgSDyY_rVA)
- Substack (also feeds Spotify and Apple Podcasts): [Ep. 3 post](https://lashawnfofung.substack.com/p/career-pivot-ep-3-from-nurse-to-scrum)
- Start here: [The Real Process Behind My Work](https://lashawnfofung.substack.com/p/start-here)

## How it works

```text
STRATEGY        Content plan → 90-day plan, KPIs, monetization strategy
   ↓
BRAND SYSTEM    Two brands: navy "LF" (professional) and green/orange "Unfiltered" (content)
   ↓
AGENT           Career Pivot Episode skill: 8 stages, 5 human approval gates
                Audio/video pipeline: clean voiceover → align → music bed → render
   ↓
DISTRIBUTION    YouTube → Substack podcast → Spotify + Apple (RSS) → LinkedIn → GitHub
   ↓
FEEDBACK        Asset log, KPIs → back into the plan
```

| Stage | Agent does | I do | Gate |
| --- | --- | --- | --- |
| 1. Interview | Writes the episode doc and 5 interview questions | Answer by voice | ✅ Approve notes |
| 2. Script | Writes a hook + 5 points + close script and a scene plan | Record one voice memo per part | ✅ Approve script |
| 3. Voiceover | Cuts slates, tightens pauses, cleans and masters to −16 LUFS, aligns words to the script | | |
| 4. Video | Builds the long-form (1920×1080) and 2 Shorts (1080×1920) with a ducked music bed, master −14 LUFS | Review renders | ✅ Approve renders |
| 5. Images | Thumbnails (+ A/B variant), Short covers, square community image, Substack header, podcast art | | |
| 6. Publishing kit | Titles, descriptions with chapters, community posts, poll, schedule | Upload to YouTube | ✅ Send the video link |
| 7. Packaging | Substack podcast draft (feeds Spotify and Apple), LinkedIn post | Add the video file, publish | ✅ Approve each post |
| 8. Cross-link + log | Links every platform to the others, updates the asset log and plan | | |

## Why five approval gates

The agent never publishes, posts or sends on its own. Each gate is where judgment matters most: my real words, accuracy, tone, and anything public. The gates have already caught a closing line that implied something untrue; it was fixed before it went live. That's the point of human-in-the-loop design.

**Guardrails built into the agent:**

- No employer names, internal numbers or projects in public content
- No patient details
- Facts and numbers come only from my interview answers; gaps become open questions
- One brand system and one title format on every platform

## What's in this repo

| Path | What it is |
| --- | --- |
| [`skills/career-pivot-episode/SKILL.md`](skills/career-pivot-episode/SKILL.md) | The agent's instructions: stages, gates, specs and guardrails (a Claude skill) |
| [`pipeline/vo_master.py`](pipeline/vo_master.py) | Voiceover mastering: trim, de-noise, EQ, de-ess, compress, two-pass loudness to −16 LUFS |
| [`pipeline/vo_align.py`](pipeline/vo_align.py) | Removes the spoken slate, tightens long pauses with crossfades, gets word timings (pocketsphinx) |

### Run the audio pipeline

Requires Python 3.10+, `ffmpeg`, `numpy` and `pocketsphinx`.

```bash
pip install numpy pocketsphinx
# vo/map.json maps part numbers to your recordings: {"1": "part1.m4a", "2": "part2.m4a"}
python pipeline/vo_master.py   # → vo/01.wav, vo/02.wav … and vo/info.json (durations, pauses)
python pipeline/vo_align.py    # → vo/01_final.wav … with word timings added to vo/info.json
```

## Skills this demonstrates

AI product management (where AI acts vs. where humans decide) · agent and workflow design · audio/video automation · brand and content strategy · cross-platform distribution · program delivery with stage gates.

## Roadmap

- [x] Career Pivot Episode agent (Ep. 3 shipped Nov 2026)
- [ ] Time and gate-catch metrics per episode
- [ ] n8n agents: Case Generator, Case Reps Scorer, Scorecard Updater, voice Mock Interviewer

---

Don't just do it. Learn it. Apply it. Grow it. Repeat. · [Substack](https://lashawnfofung.substack.com)
