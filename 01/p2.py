from inputs import Direction, cli_input


def main():
    problem = cli_input()

    num_zeroes = 0
    dial_position = 50
    problem.log(f"The dial starts by point at {dial_position}.")
    for rotation in problem.instructions:
        direction = rotation.direction
        distance = rotation.distance

        # How many clicks before zero going in the indicated direction
        # Modulo 100 because if we're travelling right and we're at zero the distance should be 0.
        distance_from_zero = (dial_position if direction == Direction.LEFT
                              else 100 - dial_position) % 100

        # Number of 0 clicks on this instruction
        # For every complete revolution, the dial visits zero once.
        zero_clicks = distance // 100
        # It visits it once more if the remaining distance after all full revolutions passes zero.
        if distance_from_zero != 0 and (distance % 100) >= distance_from_zero:
            zero_clicks += 1

        num_zeroes += zero_clicks

        # Update the dial position
        effective_direction = -1 if direction == Direction.LEFT else 1
        dial_position = (dial_position + distance * effective_direction) % 100

        problem.log(
            f"The dial is rotated {rotation} to point at {dial_position}. It visited 0 {zero_clicks} times.")

    print(f"The dial points at 0 {num_zeroes} times.")


if __name__ == "__main__":
    main()
