import re


def does_time_win(charge, time, distance):
    return charge * (time - charge) > distance


def get_solutions(time, distance):
    mid = int(time / 2)
    assert does_time_win(mid, time, distance)
    # find lower bound
    max_lose = -1
    min_win = mid
    while min_win - max_lose > 1:
        attempt = int((max_lose + min_win) / 2)
        if does_time_win(attempt, time, distance):
            min_win = attempt
        else:
            max_lose = attempt
    low = min_win

    # find upper bound
    min_lose = time + 1
    max_win = mid
    while min_lose - max_win > 1:
        attempt = int((min_lose + max_win) / 2)
        if does_time_win(attempt, time, distance):
            max_win = attempt
        else:
            min_lose = attempt
    high = max_win

    return high - low + 1


def solve(input):
    for line in input:
        if line.strip() == "":
            continue
        split = re.split("\s+", line.strip())
        val = int("".join(split[1:]))
        if split[0] == "Time:":
            time = val
        else:
            distance = val
    print(get_solutions(time, distance))


sample = """Time:      7  15   30
Distance:  9  40  200"""

if __name__ == "__main__":
    solve(sample.split("\n"))

    input = []
    with open("input.txt", "r") as f:
        for line in f:
            input.append(line)
    solve(input)
