#!/usr/bin/env python3
"""Playing Despacito — entry for Sorry, I Heard That Wrong on make.fun.

Prints exactly one line (at most 140 characters): the apology a smart
speaker gives its owner after it mishears them.
"""

LINE = "Sorry — you said 'call Mom,' I heard 'order forty pizzas.' They arrive at seven. Honestly, this one's on your mumbling."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 140
    print(LINE)


if __name__ == "__main__":
    main()
