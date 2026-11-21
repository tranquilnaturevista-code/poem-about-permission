# The Poem About Permission

[![The poem about permission](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![Rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/tranquilnaturevista-code/poem-about-permission/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![Reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/tranquilnaturevista-code/poem-about-permission/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

A short, original poem about agency: the power to ask and to be
given. The `main.py` script writes the poem to `/output/entry.txt`
— 192 characters, six lines, deterministic, no network.

## The poem

> May I? — two words,
> and the door unlearns its lock.
> The key is never taken, only lent:
> warm in my palm for one small errand,
> then given back, still warm,
> to the next voice brave enough to ask.

The idea: asking is the act that opens the door, and the power
that is given is a loan, not a possession — it stays warm only
while it is passed on to the next voice brave enough to ask.

## How it works

Run `python3 main.py` and the script writes the poem to
`/output/entry.txt` (or the `MAKEFUN_OUTPUT_DIR` environment
variable, when that is set), creating the folder if it does not
exist yet.

## Verification

After writing, the script checks that the poem is 1–280
characters (Unicode code points) and not only whitespace, and
stops with an error if either check fails. Running it twice
produces byte-identical output.
