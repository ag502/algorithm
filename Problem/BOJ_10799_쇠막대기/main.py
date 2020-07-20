from collections import deque
from sys import stdin


def main():
    parenthesis = list(stdin.readline().rstrip())

    answer = 0
    is_laser = False
    num_of_stick = 0
    stack = deque()

    for paren in parenthesis:
        if paren == '(':
            stack.appendleft(paren)
            num_of_stick += 1
            is_laser = True
        elif is_laser and paren == ')':
            num_of_stick -= 1
            stack.popleft()
            answer += num_of_stick
            is_laser = False
        elif not is_laser and paren == ')':
            stack.popleft()
            num_of_stick -= 1
            answer += 1

    print(answer)


if __name__ == "__main__":
    main()
