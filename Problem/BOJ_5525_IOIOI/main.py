from sys import stdin

def main():
    n = int(stdin.readline())
    length_of_s = int(stdin.readline())
    s = stdin.readline().rstrip()

    answer = 0
    index = 0

    while True:
        is_wrong = False
        if index > len(s) - (2 * n + 1):
            break
        if s[index] == "I" and s[index + 1] == "O":
            is_I = False
            for i in range(2 * n - 1):
                if s[index + 2 + i] == "I":
                    if is_I:
                        is_wrong = True
                        break
                    else:
                        is_I = not is_I
                elif s[index + 2 + i] == "O":
                    if not is_I:
                        is_wrong = True
                        break
                    else:
                        is_I = not is_I

            if not is_wrong:
                answer += 1
            index += 2 * n
            continue
        index += 1

    print(answer)

if __name__ == '__main__':
    main()
