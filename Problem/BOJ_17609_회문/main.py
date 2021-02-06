from sys import stdin


def check_string(string, count):
    if len(string) == 1 or count >= 2:
        return 2

    left_ptr = 0
    right_ptr = len(string) - 1

    while left_ptr <= right_ptr:
        left_char = string[left_ptr]
        right_char = string[right_ptr]

        if left_char == right_char:
            left_ptr += 1
            right_ptr -= 1
        else:
            left_remove = check_string(string[left_ptr:right_ptr], count + 1)
            right_remove = check_string(string[left_ptr + 1:right_ptr + 1], count + 1)
            return 1 if left_remove == 1 or right_remove == 1 else 2

    if count == 1:
        return 1
    return 0


def main():
    stdin = open("./input.txt", "r")
    test_case = int(stdin.readline())

    for _ in range(test_case):
        string = stdin.readline().rstrip()
        print(check_string(string, 0))


if __name__ == '__main__':
    main()