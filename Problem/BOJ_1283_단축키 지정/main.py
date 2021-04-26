from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    num_of_alphabet = int(stdin.readline())

    shortcut_list = set()
    for _ in range(num_of_alphabet):
        cur_option = stdin.readline().rstrip()
        words = cur_option.split(' ')
        for idx, word in enumerate(words):
            if word[0].lower() not in shortcut_list:
                words[idx] = "[" + word[0] + "]" + word[1:]
                shortcut_list.add(word[0].lower())
                break
        else:
            answer = ''
            is_add = False
            for char in cur_option:
                if char == ' ':
                    answer += char
                else:
                    if char.lower() in shortcut_list:
                        answer += char
                    else:
                        if not is_add:
                            shortcut_list.add(char.lower())
                            answer += "[" + char + "]"
                            is_add = True
                        else:
                            answer += char

            print(answer)
            continue
        print(' '.join(words))
        continue


if __name__ == '__main__':
    main()