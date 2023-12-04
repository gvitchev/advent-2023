import re
import functools
import operator


def line_val(line):
    vals = line.split(":")[1]
    win, have = vals.split("|")
    win = {int(x) for x in re.split("\s+", win.strip())}
    result = 0
    for i in re.split("\s+", have.strip()):
        if int(i) in win:
            result += 1
    return result


def solve(input):
    counts = [1 for x in range(len(input))]
    for i, line in enumerate(input):
        val = line_val(line)
        for j in range(i + 1, i + 1 + val):
            if j < len(counts):
                counts[j] += counts[i]
    return functools.reduce(operator.add, counts, 0)


samples = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

if __name__ == "__main__":
    print(solve(samples.splitlines()))
    pass

    input = []
    with open("input.txt", "r") as f:
        for line in f:
            input.append(line)
    print(solve(input))
