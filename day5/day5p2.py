import re
import sys


def pp(num):
    print("{:,}".format(num))


def find_ranges_for_single_range(range, mappings):
    # mappings are sorted by start of range
    result = []
    idx, remaining = range
    for dest_start, mapping_start, mapping_count in mappings:
        mapping_end = mapping_start + mapping_count
        if idx > mapping_end:
            continue
        if mapping_start >= idx + remaining:
            result.append((idx, remaining))
            remaining = 0
            break
        if mapping_start > idx:
            result.append((idx, mapping_start - idx))
            remaining -= mapping_start - idx
            idx = mapping_start
        idx_dest_val = dest_start + idx - mapping_start
        if idx + remaining <= mapping_end:
            result.append((idx_dest_val, remaining))
            remaining = 0
            break
        else:
            result.append((idx_dest_val, mapping_end - idx))
            remaining -= mapping_end - idx
            idx = mapping_end
    if remaining > 0:
        result.append((idx, remaining))
    return result


def find_ranges(ranges, mappings):
    result = []
    for range in ranges:
        result += find_ranges_for_single_range(range, mappings)
    return result


def find_seed_range_value(range, maps):
    current_ranges = [range]
    current_type = "seed"
    while True:
        if current_type not in maps:
            lowest = sys.maxsize
            for x, y in current_ranges:
                if x < lowest:
                    lowest = x
            return lowest
        current_ranges = find_ranges(current_ranges, maps[current_type][1])
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
            maps[source] = [to, []]
            current = source
            continue
        maps[current][1].append([int(x) for x in line.strip().split(" ")])

    # sort by source id
    for k in maps:
        maps[k][1] = sorted(maps[k][1], key=lambda x: x[1])

    min = sys.maxsize
    for i in range(int(len(seeds) / 2)):
        start = seeds[2 * i]
        count = seeds[2 * i + 1]
        val = find_seed_range_value((start, count), maps)
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
    with open("/Users/gvitchev/advent-2023/day5/input.txt", "r") as f:
        for line in f:
            input.append(line)
    solve(input)
