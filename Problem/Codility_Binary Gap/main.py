from collections import deque


def solution(N):
    binary_num = bin(N)[2:]
    queue = deque(binary_num)

    is_open = False
    binary_gap = 0

    temp = 0
    while queue:
        cur_num = queue.popleft()
        if cur_num == "1":
            if is_open:
                binary_gap = max(binary_gap, temp)
                temp = 0
            else:
                is_open = True
        else:
            temp += 1

    return binary_gap


if __name__ == '__main__':
    print(solution(1610612737))