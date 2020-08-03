from sys import stdin


def get_cyclic_word(word, start):
    length = len(word)
    string = ''
    while len(string) != length:
        string += word[start % length]
        start += 1
    return string


def main():
    word_set = set()
    num_of_word = int(stdin.readline())

    for _ in range(num_of_word):
        word = stdin.readline().rstrip()
        if not word_set:
            word_set.add(word)
        else:
            for i in range(len(word)):
                if get_cyclic_word(word, i) in word_set:
                    break
            else:
                word_set.add(word)
    print(len(word_set))


if __name__ == "__main__":
    main()
