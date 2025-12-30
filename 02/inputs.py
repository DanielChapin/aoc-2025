from argparse import ArgumentParser, BooleanOptionalAction
from dataclasses import dataclass
import re
from sys import argv


@dataclass
class InRange:
    lo: int
    hi: int

    def __str__(self) -> str:
        return f"{self.lo}-{self.hi}"

    @staticmethod
    def from_str(s: str) -> "InRange":
        m = re.fullmatch(r"\s*(\d+)-(\d+)\s*", s)
        if m is None:
            raise ValueError(f"Could not parse input range from '{s}'")

        return InRange(int(m.group(1)), int(m.group(2)))


def parser() -> ArgumentParser:
    p = ArgumentParser()

    p.add_argument("input_file", help="File containing ID ranges.")
    p.add_argument("--debug", "-d", default=False, action=BooleanOptionalAction,
                   help="Print out steps.")

    return p


@dataclass
class Day2Input:
    ranges: list[InRange]
    debug: bool

    def log(self, *args, **kwargs) -> None:
        if self.debug:
            print(*args, **kwargs)


def cli_input(args: list[str] = argv[1:]) -> Day2Input:
    cfg = parser().parse_args(args)

    with open(cfg.input_file, "r") as input_file:
        lines = [line.strip() for line in input_file.readlines()]
        vals = [
            val
            for line in lines
            for val in line.split(',')
        ]
        ranges = [InRange.from_str(val) for val in vals if val != ""]
        return Day2Input(ranges, cfg.debug)
