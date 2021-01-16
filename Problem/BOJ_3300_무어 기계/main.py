from sys import stdin
import re


def main():
    stdin = open('./input.txt', 'r')
    test_case = int(stdin.readline())

    for _ in range(test_case):
        machine = stdin.readline().strip()
        output = stdin.readline().strip()

        match_count = 0
        match_char = ''
        for code in range(ord('A'), ord('Z') + 1):
            new_machine = machine.replace("_", chr(code))
            regex = re.compile("^" + new_machine + "$")

            if regex.match(output) is not None:
                match_count += 1
                match_char = chr(code)

        if match_count == 0:
            print("!")
        elif match_count == 1:
            print(match_char)
        else:
            print("_")


if __name__ == '__main__':
    main()