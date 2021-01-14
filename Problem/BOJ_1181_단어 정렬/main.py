from sys import stdin


def main():
    stdin = open('./input.txt')
    num_of_words = int(stdin.readline())
    words = {}

    for _ in range(num_of_words):
        word = stdin.readline().strip()
        words[word] = len(word)

    words = sorted(words.items(), key=lambda x: (x[1], x[0]))

    for word, length in words:
        print(word, len(word))


if __name__ == '__main__':
    main()