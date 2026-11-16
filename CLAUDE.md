# CLAUDE.md

Instructions for Claude Code in this repo. Claude Code reads this file at the start of every session.

## What this repo is

The AI Content Ops Agent: a human-in-the-loop system that turns one voice recording into a long-form video, 2 Shorts, a podcast episode and social posts for Lashawn Fofung's **Career Pivot** series.

- The agent's workflow lives in `.claude/skills/career-pivot-episode/SKILL.md`. Claude Code loads it as a project skill. Start an episode with: "Run Career Pivot Ep. N".
- The audio pipeline lives in `pipeline/`: `vo_master.py`, then `vo_align.py`.

## Rules (always)

- **Never publish, post, send or schedule anything** without Lashawn's explicit yes for that item. Stop at every gate in the skill.
- **Facts come only from her interview answers.** Never invent dates, numbers or stories; list gaps as open questions.
- **Keep the current employer vague.** No employer name, internal numbers or projects. Say "healthcare technology" or "my current role."
- **No patient details.** Say "insurance plans," not "Medicare."
- **Her voice, not a synthetic one.** Clean and time her recordings; fix a wrong value in on-screen text, never by editing her audio.
- **One title format:** "Career Pivot — Ep. N: <Outcome title>".

## Working in this repo

- Never commit voice recordings, renders, drafts, resumes, API keys or personal contact details. Working files (`vo/`, renders, images) stay local.
- Python 3.10+, `ffmpeg`, `numpy`, `pocketsphinx`. Run scripts from the folder that contains `vo/`.
- Audio targets: voiceover −16 LUFS; final mix −14 LUFS, −1 dBTP.
- Keep the README in the same format as Lashawn's other portfolio repos (centered header with badges, Contents, TL;DR table, Key Product Decisions, Architecture, My Role, Related Repos, centered footer).
