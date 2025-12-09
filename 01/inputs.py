from dataclasses import dataclass
from enum import Enum
import re
from argparse import BooleanOptionalAction, ArgumentParser
from sys import argv


class Direction(Enum):
    LEFT = 0
    RIGHT = 1

    def __str__(self) -> str:
        return "L" if self == Direction.LEFT else "R"

    @staticmethod
    def from_str(s: str) -> "Direction":
        match s.lower():
            case "l":
                return Direction.LEFT
            case "r":
                return Direction.RIGHT
            case s:
                raise ValueError(f"Couldn't parse direction from {s}")


@dataclass
class Rotation:
    direction: Direction
    distance: int

    def __str__(self) -> str:
        return f"{self.direction}{self.distance}"

    @staticmethod
    def from_str(s: str) -> "Rotation":
        m = re.fullmatch(r"^([LR])(\d+)$", s)
        if m is None:
            raise ValueError(f"Couldn't parse rotation from {s}")

        direction = Direction.from_str(m.group(1))
        distance = int(m.group(2))

        return Rotation(direction, distance)


def parser() -> ArgumentParser:
    p = ArgumentParser()

    p.add_argument("input_file", help="File containing Elf safe instructions.")
    p.add_argument("--debug", "-d", default=False, action=BooleanOptionalAction,
                   help="Print out steps.")

    return p


@dataclass
class Day1Input:
    instructions: list[Rotation]
    debug: bool

    def log(self, *args, **kwargs) -> None:
        if self.debug:
            print(*args, **kwargs)


def cli_input(args: list[str] = argv[1:]) -> Day1Input:
    cfg = parser().parse_args(args)

    with open(cfg.input_file, "r") as input_file:
        lines = [line.strip() for line in input_file.readlines()]
        instructions = [Rotation.from_str(line)
                        for line in lines if line != ""]
        return Day1Input(instructions, cfg.debug)
