from sys import stdin


def main():
    while True:
        word = stdin.readline().rstrip()
        if word == '*':
            break

        if len(word) == 1:
            print('{} is surprising.'.format(word))
        else:
            for i in range(0, len(word) - 1):
                word_set = set()
                for j in range(0, len(word) - (i + 1)):
                    word_set.add(word[j] + word[j + i + 1])
                if len(word_set) != len(word) - (i + 1):
                    print('{} is NOT surprising.'.format(word))
                    break
            else:
                print('{} is surprising.'.format(word))


if __name__ == "__main__":
    main()
