from sys import stdin
from collections import deque

MAX = 100000

def main():
    n, k = map(int, stdin.readline().split())
    queue = deque()
    visited = set()
    depth = 0
    queue.append([depth, n])
    visited.add(n)

    while True:
        time, cur_pos = queue.popleft()
        if cur_pos == k:
            print(time)
            return

        depth = time + 1
        if 0 <= cur_pos - 1 <= MAX and cur_pos - 1 not in visited:
            queue.append([depth, cur_pos - 1])
            visited.add(cur_pos - 1)
        if 0 <= cur_pos + 1 <= MAX and cur_pos + 1 not in visited:
            queue.append([depth, cur_pos + 1])
            visited.add(cur_pos + 1)
        if 0 <= cur_pos * 2 <= MAX and cur_pos * 2 not in visited:
            queue.append([depth, cur_pos * 2])
            visited.add(cur_pos * 2)

if __name__ == '__main__':
    main()
