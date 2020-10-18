from sys import stdin
from collections import deque

def main():
    # stdin = open('./test_case.txt', 'r')
    f, s, g, u, d = map(int, stdin.readline().split())
    queue = deque()
    visited = [False] * 1000001

    queue.append(s)
    visited[s] = True
    push_count = 0

    while len(queue) != 0:
        size = len(queue)

        for _ in range(size):
            cur_stair = queue.popleft()

            if cur_stair == g:
                print(push_count)
                return

            # 갈 수 있는 층 탐색
            next_up_stair = cur_stair + u
            next_down_stair = cur_stair - d

            if 0 < next_up_stair <= f and not visited[next_up_stair]:
                queue.append(next_up_stair)
                visited[next_up_stair] = True
            if 0 < next_down_stair <= f and not visited[next_down_stair]:
                queue.append(next_down_stair)
                visited[next_down_stair] = True

        push_count += 1

    print('use the stairs')

if __name__ == '__main__':
    main()

