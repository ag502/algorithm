from sys import stdin
from collections import deque

def main():
    stdin = open('./test_case.txt', 'r')

    operation = stdin.readline().rstrip()
    stack = deque()

    num_str = ''
    is_plus = False
    for char in operation:
        if char == '-' or char == '+':
            if is_plus:
                cur_num = stack.pop()
                stack.append(cur_num + int(num_str))
            else:
                stack.append(int(num_str))

            if char == '-':
                is_plus = False
            else:
                is_plus = True

            num_str = ''
        else:
            num_str += char

    if is_plus:
        cur_num = stack.pop()
        stack.append(cur_num + int(num_str))
    else:
        stack.append(int(num_str))

    answer = stack.popleft()
    while len(stack) != 0:
        answer -= stack.popleft()

    print(answer)

if __name__ == '__main__':
    main()
