from sys import stdin
from collections import deque

operator_priority = {"*": 1, "/": 1, "+": 2, "-": 2, "(": 3}


def main():
    stdin = open("./input.txt", "r")
    expression = stdin.readline().rstrip()

    operator_stack = deque()
    answer = []

    for char in expression:
        if ord('A') <= ord(char) <= ord('Z'):
            answer.append(char)
        else:
            if not operator_stack:
                operator_stack.append(char)
            else:
                if char == "(":
                    operator_stack.append(char)
                elif char == ")":
                    while True:
                        cur_op = operator_stack.pop()
                        if cur_op == "(":
                            break
                        answer.append(cur_op)
                else:
                    while True:
                        if not operator_stack:
                            operator_stack.append(char)
                            break
                        top = operator_stack[len(operator_stack) - 1]
                        if operator_priority[top] <= operator_priority[char]:
                            answer.append(operator_stack.pop())
                            continue
                        operator_stack.append(char)
                        break

    while operator_stack:
        answer.append(operator_stack.pop())

    print(''.join(answer))


if __name__ == '__main__':
    main()