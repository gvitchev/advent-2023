import re
import sys


def find_value(val, mappings):
    for dest_start, source_start, range in mappings:
        diff = val - source_start
        if diff >= 0 and diff < range:
            return dest_start + diff
    return val


def find_seed_value(seed, maps):
    current_type = "seed"
    current_val = seed
    while True:
        if current_type not in maps:
            return current_val
        current_val = find_value(current_val, maps[current_type][1])
        current_type = maps[current_type][0]


def solve(lines):
    maps = {}
    for line in lines:
        line = line.strip()
        if len(line) == 0:
            continue
        if line.startswith("seeds:"):
            line = line.removeprefix("seeds:")
            seeds = [int(x) for x in line.strip().split(" ")]
            continue
        match = re.compile(r"^([a-z]+)-to-([a-z]+)\smap:").match(line)
        if not match is None:
            source, to = match.group(1), match.group(2)
            maps[source] = (to, [])
            current = source
            continue
        maps[current][1].append([int(x) for x in line.strip().split(" ")])

    min = sys.maxsize
    for seed in seeds:
        val = find_seed_value(seed, maps)
        if val < min:
            min = val

    print(min)


sample = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

if __name__ == "__main__":
    solve(sample.split("\n"))

    input = []
    with open("input.txt", "r") as f:
        for line in f:
            input.append(line)
    solve(input)
