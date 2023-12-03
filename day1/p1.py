def solve():
    sum = 0
    with open("input.txt", "r") as f:
        for line in f:
            sum += val(line)
    return sum


WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def val(line):
    first, last = None, None
    current_words = {}
    for c in line:
        if c >= "0" and c <= "9":
            if first is None:
                first = int(c)
            last = int(c)
        else:
            new_current_words = {}
            for word in WORDS:
                if word[0] == c:
                    new_current_words[word[1:]] = WORDS[word]
            for word in current_words:
                if word[0] == c:
                    if len(word) == 1:
                        val = current_words[word]
                        if first is None:
                            first = val
                        last = val
                    else:
                        new_current_words[word[1:]] = current_words[word]
            current_words = new_current_words
    return 10 * first + last


if __name__ == "__main__":
    print(solve())
    # print(val("two1nine"))
    # print(val("eightwothree"))
    # print(val("abcone2threexyz"))
    # print(val("xtwone3four"))
    # print(val("4nineeightseven2"))
    # print(val("zoneight234"))
    # print(val("7pqrstsixteen"))
