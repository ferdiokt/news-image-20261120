# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/ferdiokt/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/ferdiokt/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A one-image summary of the world's news for **Friday 20 November 2026**: 23 stories from 6 regions, each
confirmed by at least two named outlets and tagged REPORTED, CLAIM or FORECAST.

- `stories.py`: the story ledger (place, region, field, tag, local time, headline, fact, source URLs) with an
  assert-based self-check (2+ outlets per story, headlines of 8 words max, 5+ regions).
- `render.py`: draws `entry.png` from the ledger with Pillow (flat drawings in code, every word typeset in code)
  and writes `SOURCES.md`, including big stories from other days that were deliberately left out.
- `main.py`: the entrypoint. Standard library only, offline: it checks the committed PNG and copies it to
  `$MAKEFUN_OUTPUT_DIR` (default `/output`), byte for byte.

![Friday, 20 November 2026](entry.png)

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py     # writes out/entry.png
python3 render.py                          # optional: redraw entry.png + SOURCES.md (needs Pillow, URW base35 fonts)
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
