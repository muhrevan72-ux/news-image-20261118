[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/muhrevan72-ux/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/muhrevan72-ux/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

# One Image, One Day — 18 November 2026

A newspaper front page for Wednesday 18 November 2026, made for the
make.fun bounty
[Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118).
One image, 1024 × 1024, that has to carry the whole day on its own.

## The stories on the page

**Lead — Middle East:** Iran strikes Kuwait & Bahrain, hitting US
bases in the Gulf after US aircraft struck a missile site on
Qeshm Island.

**Geopolitics:** Xi and Putin meet in Shenzhen, ahead of Thursday's
trilateral talks with Trump.

**Europe:** the Crimea Bridge is hit again — part of its road span
collapses on the second day of strikes.

**US politics:** Mary Peltola wins the Alaska Senate seat, giving
Democrats a 56–44 majority.

**Health:** the US loses its measles-free status after 26 years,
with more than 5,400 cases reported.

**Tech & economy:** Nvidia doubles revenue to $115.8bn, and its
board rules out bringing back Jensen Huang as CEO.

**Middle East:** Israel's parliament elects Matan Kahana as the
new Knesset speaker.

**Also today:** Ebola in DR Congo passes 11,000 cases; the Quad
meets in Manila; a Russian plane crashes in Siberia, 19 dead.

Everything above was reported on 18 November 2026 (AFP, AP,
Reuters, Just Security). Nothing on the page is invented, and no
rumour is presented as fact.

## Files

- `main.py` — the entry program. Python 3.13, standard library
  only, no network. It copies `entry.png` to the output folder
  the grader gives it, byte for byte.
- `entry.png` — the finished front page, 1024 × 1024 PNG.
- `render.py` — the local tool that draws the page with Pillow
  and DejaVu fonts. It is not part of grading.
- `LICENSE` — MIT.

## Try it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Local checks, 19 Nov 2026

- Ran `main.py` twice: both outputs byte-identical.
- Image is 1024 × 1024 PNG, well under the 1 MiB limit.
- Read the finished image: every headline and summary is
  legible, nothing is cut off, nothing is garbled.
