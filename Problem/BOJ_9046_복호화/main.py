from sys import stdin
from collections import Counter


def main():
    stdin = open("./input.txt", "r")

    test_case = int(stdin.readline())

    for _ in range(test_case):
        password = stdin.readline().rstrip().replace(" ", "")
        word_freq = Counter(password).most_common(2)

        if len(word_freq) >= 2 and word_freq[0][1] == word_freq[1][1]:
            print("?")
        else:
            print(word_freq[0][0])


if __name__ == '__main__':
    main()