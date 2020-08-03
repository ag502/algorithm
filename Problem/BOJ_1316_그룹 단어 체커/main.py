from sys import stdin


def main():
    test_case = int(stdin.readline())
    answer = 0

    for _ in range(test_case):
        word = stdin.readline().rstrip()

        char_set = set()
        prev_word = ''
        for char in word:
            cur_word = char

            if prev_word != cur_word:
                if cur_word not in char_set:
                    char_set.add(cur_word)
                else:
                    break
            prev_word = cur_word
        else:
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
