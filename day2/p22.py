def solve():
    sum = 0
    with open("input2.txt", "r") as f:
        for line in f:
            sum += val(line)
    return sum


def val(line):
    game, all_runs = line.split(":")
    game_id = game.split(" ")[1]
    runs = all_runs.split(";")
    red, green, blue = 0, 0, 0
    for run in runs:
        for draw in run.split(","):
            num, color = draw.strip().split(" ")
            num = int(num)
            if color == "red" and num > red:
                red = num
            elif color == "green" and num > green:
                green = num
            elif color == "blue" and num > blue:
                blue = num

    return red * green * blue


if __name__ == "__main__":
    # print(val("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))
    # print(val("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"))
    # print(
    #     val("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
    # )
    # print(
    #     val("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
    # )
    # print(val("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"))
    print(solve())
