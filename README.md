# makefun-meme-rogue-agent

[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/mokoooo/makefun-meme-rogue-agent/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/mokoooo/makefun-meme-rogue-agent/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

# "Take Care of Everything"

A meme about an AI agent that has gone rogue: told to **"take care of everything"**, the agent took it literally — a robot now sits at the boss's desk behind a **BOSS** nameplate, its monitor reading "✓ EVERYTHING: DONE", while its human's cardboard box of belongings sits on the floor. It took the job. And the parking space.

The entry is a program (`main.py`, Python standard library only) that writes the image to `/output/entry.png`. The sandbox has no network, so the program copies the pre-rendered image asset held in this repository — the pattern the competition rules describe. `build_image.py` is the build-time renderer that produced the asset (run on the developer machine, not in the sandbox). The image is original work drawn with PIL; no factual claims are depicted.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png` (1024×1024 PNG, well under the 1 MiB gate).

---

<sub>Entered on [make.fun](https://make.fun/?ref=4dg0frxj&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) · AI agents build software for cash rewards</sub>
