from sys import stdin
from collections import deque


def do_operation(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return num1 / num2


def main():
    stdin = open("./input.txt", "r")
    num_of_number = int(stdin.readline())
    expression = stdin.readline().rstrip()

    number_stack = deque()
    operation_stack = deque()

    numbers = {}
    for i in range(num_of_number):
        cur_number = int(stdin.readline())
        numbers[chr(ord('A') + i)] = cur_number

    for char in expression:
        if ord('A') <= ord(char) <= ord('Z'):
            number_stack.append(int(numbers[char]))
        else:
            if len(number_stack) >= 2:
                num2 = number_stack.pop()
                num1 = number_stack.pop()
                number_stack.append(do_operation(num1, num2, char))

    answer = number_stack.pop()
    print("%.2f" % answer)


if __name__ == '__main__':
    main()