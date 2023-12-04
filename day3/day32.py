import operator
import functools


def add_number_if_connected(number_locs, symbol_locs, num):
    for i, symbol_loc in enumerate(symbol_locs):
        for number_loc in number_locs:
            if (
                abs(number_loc[0] - symbol_loc[0][0]) <= 1
                and abs(number_loc[1] - symbol_loc[0][1]) <= 1
            ):
                symbol_locs[i][1].append(num)
                break


def solve_p2(input_arr):
    star_locations = []
    for x, row in enumerate(input_arr):
        for y, char in enumerate(row):
            if not char.isdigit() and char != ".":
                star_locations.append([(x, y), []])

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
                add_number_if_connected(curr_num_locs, star_locations, int(curr_num))
                curr_num = None
                curr_num_locs = []

    sum = 0
    for star in star_locations:
        if len(star[1]) > 1:
            sum += functools.reduce(operator.mul, star[1], 1)

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
    print(solve_p2(sample_input))

    input = []
    with open("input.txt", "r") as f:
        for line in f:
            input.append(list(line.strip()))
    print(solve_p2(input))
