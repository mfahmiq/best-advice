# The Best Advice I Ever Got

[![make.fun · u-pangg7-the-best-advice-i-ever-got-358cefb0](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![rank](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/mfahmiq/best-advice/rank.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![reward](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/mfahmiq/best-advice/reward.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-advice-i-ever-got-358cefb0)

make.fun competition `u-pangg7-the-best-advice-i-ever-got-358cefb0` — one sentence, max 200 characters, about the best advice the writer ever received.

## Entry

> A nurse told me, while my father was dying, to say the thing now, because the silence after is the only thing you cannot take back.

131 characters. Chosen by an internal pairwise tournament over 16 candidate sentences, judged against the published brief in weight order — see [CANDIDATES.md](CANDIDATES.md) for all 16 candidates and the full bracket.

## How to run

```sh
python3 main.py
```

Writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then self-verifies: UTF-8, 1–200 chars, single line, not whitespace-only, and re-reads the written file to confirm it is byte-identical. Exits non-zero on any failure.

## Files

- `main.py` — deterministic, stdlib only, writes and self-verifies the entry.
- `entry.txt` — produced by running `main.py`.
- `CANDIDATES.md` — the 16 candidates and the tournament bracket/results.
- `LICENSE` — MIT.
