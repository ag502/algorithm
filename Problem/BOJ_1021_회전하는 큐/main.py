from sys import stdin
from collections import deque


def main():
    n, m = map(int, stdin.readline().split())
    pop_num = list(map(int, stdin.readline().split()))
    queue = deque([i for i in range(1, n + 1)])

    num_of_cycle = 0

    for number in pop_num:
        find_idx = 0
        for idx, num in enumerate(queue):
            if num == number:
                find_idx = idx
                break
        if find_idx <= len(queue) // 2:
            while queue[0] != number:
                queue.append(queue.popleft())
                num_of_cycle += 1
            queue.popleft()
        else:
            while queue[0] != number:
                queue.appendleft(queue.pop())
                num_of_cycle += 1
            queue.popleft()
    print(num_of_cycle)


if __name__ == "__main__":
    main()
