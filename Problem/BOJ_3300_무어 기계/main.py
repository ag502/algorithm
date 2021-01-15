from sys import stdin
import re


def parsing_machine(machine):
    new_machine = ["^"]
    for char in machine:
        if char == "(":
            new_machine.append("(?:")
        elif char == "_":
            new_machine.append("([A-Z])")
        else:
            new_machine.append(char)
    new_machine.append("$")
    return "".join(new_machine)


def main():
    stdin = open('./input.txt', 'r')
    test_case = int(stdin.readline())

    for _ in range(test_case):
        machine = stdin.readline().strip()
        output = stdin.readline().strip()

        regex = re.compile(parsing_machine(machine))
        is_contained = regex.match(output)

        if is_contained is None:
            print("!")
        else:
            if is_contained.group(1) is None:
                print("_")
            else:
                print(is_contained.group(1))


if __name__ == '__main__':
    main()