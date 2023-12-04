import re


def line_val(line):
    vals = line.split(":")[1]
    win, have = vals.split("|")
    win = {int(x) for x in re.split("\s+", win.strip())}
    result = 0
    for i in re.split("\s+", have.strip()):
        if int(i) in win:
            if result == 0:
                result = 1
            else:
                result *= 2
    return result


samples = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


if __name__ == "__main__":
    sample_sum = 0
    for line in samples.splitlines():
        sample_sum += line_val(line)
    print(sample_sum)

    sum = 0
    with open("input.txt", "r") as f:
        for line in f:
            sum += line_val(line)
    print(sum)
