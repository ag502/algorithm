from sys import stdin
from collections import deque

def main():
    num_of_antenna = int(stdin.readline())
    antenna_list = list(map(int, stdin.readline().split()))
    received_top = [0] * len(antenna_list)

    stack = deque()
    stack.appendleft((1, antenna_list[0]))


    for idx in range(1, len(antenna_list)):
        top = stack[0]
        if top[1] > antenna_list[idx]:
            received_top[idx] = top[0]
            stack.appendleft((idx + 1, antenna_list[idx]))
        else:
            while True:
                stack.popleft()
                if len(stack) == 0:
                    stack.appendleft((idx + 1, antenna_list[idx]))
                    break
                else:
                    top = stack[0]
                    if top[1] <= antenna_list[idx]:
                        continue
                    else:
                        stack.appendleft((idx + 1, antenna_list[idx]))
                        received_top[idx] = top[0]
                        break

    answer_str = ''
    for top_num in received_top:
        answer_str += str(top_num) + ' '
    print(answer_str.strip())

if __name__ == '__main__':
    main()

