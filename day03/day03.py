import re


file = open("input.txt", "r")
input = file.read()


def part01(schematic):
    lines = schematic.split("\n")
    total = 0
    height = len(lines)
    width = len(lines[0]) if height > 0 else 0
    symbols = {"*", "#", "+", "$", "=", "%", "/", "@", "-", "&"}

    def is_symbol_adjacent(x, y, length):
        for i in range(length):
            if any(
                check(x + i, y)
                for check in [
                    is_symbol_left,
                    is_symbol_right,
                    is_symbol_above,
                    is_symbol_below,
                    is_symbol_diagonal_up_left,
                    is_symbol_diagonal_up_right,
                    is_symbol_diagonal_down_left,
                    is_symbol_diagonal_down_right,
                ]
            ):
                return True
        return False

    def is_symbol_left(x, y):
        return x > 0 and lines[y][x - 1] in symbols

    def is_symbol_right(x, y):
        return x < width - 1 and lines[y][x + 1] in symbols

    def is_symbol_above(x, y):
        return y > 0 and lines[y - 1][x] in symbols

    def is_symbol_below(x, y):
        return y < height - 1 and lines[y + 1][x] in symbols

    def is_symbol_diagonal_up_left(x, y):
        return x > 0 and y > 0 and lines[y - 1][x - 1] in symbols

    def is_symbol_diagonal_up_right(x, y):
        return x < width - 1 and y > 0 and lines[y - 1][x + 1] in symbols

    def is_symbol_diagonal_down_left(x, y):
        return x > 0 and y < height - 1 and lines[y + 1][x - 1] in symbols

    def is_symbol_diagonal_down_right(x, y):
        return x < width - 1 and y < height - 1 and lines[y + 1][x + 1] in symbols

    for y, line in enumerate(lines):
        matches = re.finditer(r"\b\d{1,3}\b", line)
        for match in matches:
            number = match.group()
            start = match.start()
            if is_symbol_adjacent(start, y, len(number)):
                total += int(number)

    return total


def part02(schematic):
    lines = schematic.split("\n")
    height = len(lines)
    width = len(lines[0])
    total_ratio_sum = 0
    pattern = re.compile(r"\d{1,3}")  # Pattern to find numbers up to 3 digits

    for x, line in enumerate(lines):
        for match in re.finditer("\*", line):
            gear_start, gear_stop = match.span()
            nums = []

            # Check vertically (above and below)
            for row in (1, -1):
                if 0 <= x + row < height:  # Ensure within grid bounds
                    for num_match in pattern.finditer(lines[x + row]):
                        num_start, num_stop = num_match.span()
                        if (
                            gear_start - 1 <= num_start <= gear_stop
                            or gear_start <= num_stop <= gear_stop + 1
                        ):
                            nums.append(num_match.group())

            # Check immediate left and right on the same line
            for num_match in pattern.finditer(line):
                num_start, num_stop = num_match.span()
                if num_stop == gear_start or num_start == gear_stop:
                    nums.append(num_match.group())

            # Calculate gear ratio if two numbers are found
            if len(nums) == 2:
                total_ratio_sum += int(nums[0]) * int(nums[1])

    return total_ratio_sum


print(part01(input))
print(part02(input))
