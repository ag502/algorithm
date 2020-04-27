from sys import stdin
from collections import deque

def main():
    k = int(stdin.readline())
    number_stack = deque()

    for _ in range(k):
        number = int(stdin.readline())

        if number == 0:
            number_stack.pop()
        else:
            number_stack.append(number)

    total_sum = 0

    for number in number_stack:
        total_sum += number

    print(total_sum)

if __name__ == "__main__":
    main()

