from dataclasses import dataclass
from math import ceil, log10
from inputs import cli_input
from typing import Iterable


def int_len(x: int) -> int:
    y = log10(x)
    if ceil(y) == y:
        return int(y) + 1
    return ceil(y)


@dataclass
class Id:
    kernel: int

    def __int__(self) -> int:
        return self.kernel + self.kernel * int(10 ** int_len(self.kernel))

    def to(self, end: "Id", inclusive: bool = True) -> "Iterable[Id]":
        a = self.kernel
        b = end.kernel
        if inclusive:
            b += 1

        for n in range(a, b):
            yield Id(n)


def up(x: int) -> Id:
    l = int_len(x)
    if l % 2 == 1:
        return Id(int(10 ** ((l + 1) / 2 - 1)))

    b = int(10 ** (l / 2))
    x1 = x // b
    x2 = x % b

    if x2 <= x1:
        return Id(x1)
    else:
        return Id(x1 + 1)


def down(x: int) -> Id | None:
    if x < 11:
        return None

    l = int_len(x)
    if l % 2 == 1:
        return Id(int(10 ** ((l - 1) / 2)) - 1)

    b = int(10 ** (l / 2))
    x1 = x // b
    x2 = x % b

    if x2 >= x1:
        return Id(x1)
    else:
        return Id(x1 - 1)


def main():
    problem = cli_input()

    solution = 0
    for in_range in problem.ranges:
        a, b = in_range.lo, in_range.hi
        problem.log(f"Range: {in_range}")

        ap = up(a)
        bp = down(b)
        problem.log(f"  ID Range: {ap} - {bp}")

        if bp is None:
            problem.log("  No valid upper bound.")
            continue

        for n in ap.to(bp):
            problem.log(f"  {n} ({int(n)}) in range")
            solution += int(n)

    print(f"Final sum: {solution}")


if __name__ == "__main__":
    main()
