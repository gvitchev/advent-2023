def is_number_connected(number_locs, symbol_locs):
    for symbol_loc in symbol_locs:
        for number_loc in number_locs:
            if (
                abs(number_loc[0] - symbol_loc[0]) <= 1
                and abs(number_loc[1] - symbol_loc[1]) <= 1
            ):
                return True
    return False


def solve(input_arr):
    symbol_locations = []
    for x, row in enumerate(input_arr):
        for y, char in enumerate(row):
            if not char.isdigit() and char != ".":
                symbol_locations.append((x, y))

    sum = 0
    for x, row in enumerate(input_arr):
        curr_num = None
        curr_num_locs = []
        for y, char in enumerate(row):
            if char.isdigit():
                if curr_num is None:
                    curr_num = char
                else:
                    curr_num += char
                curr_num_locs.append((x, y))

            if curr_num is not None and (y == len(row) - 1 or not char.isdigit()):
                if is_number_connected(curr_num_locs, symbol_locations):
                    sum += int(curr_num)
                curr_num = None
                curr_num_locs = []
    return sum


sample = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

if __name__ == "__main__":
    sample_input = []
    for line in sample.splitlines():
        sample_input.append(list(line.strip()))
    print(solve(sample_input))

    input = []
    with open("input.txt", "r") as f:
        for line in f:
            input.append(list(line.strip()))
    print(solve(input))
