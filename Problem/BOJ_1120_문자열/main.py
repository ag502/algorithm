from sys import stdin


def main():
    a, b = stdin.readline().rstrip().split()

    i = 0
    answer = 50
    while len(b) - i >= len(a):
        difference = 0
        for a_char, b_char in zip(a, b[i:]):
            if a_char != b_char:
                difference += 1
        if answer > difference:
            answer = difference
        i += 1
    print(answer)


if __name__ == "__main__":
    main()
