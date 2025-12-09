from inputs import Direction, cli_input


def main():
    problem = cli_input()

    num_zeroes = 0
    dial_position = 50
    problem.log(f"The dial starts by point at {dial_position}.")
    for rotation in problem.instructions:
        effective_direction = -1 if rotation.direction == Direction.LEFT else 1
        effective_distance = rotation.distance * effective_direction
        dial_position = (dial_position + effective_distance) % 100
        if dial_position == 0:
            num_zeroes += 1

        problem.log(
            f"The dial is rotated {rotation} to point at {dial_position}.")

    print(f"The dial points at 0 {num_zeroes} times.")


if __name__ == "__main__":
    main()
