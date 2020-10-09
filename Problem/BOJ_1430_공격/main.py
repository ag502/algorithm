from sys import stdin
from collections import deque


def main():
    n, r, d, e_x, e_y = map(int, stdin.readline().split())
    positions = [0, [e_x, e_y, -1]]
    for _ in range(n):
        t_x, t_y = map(int, stdin.readline().split())
        positions.append([t_x, t_y, d])

    visited = [False] * (n + 2)

    queue = deque()
    queue.append(positions[1])
    visited[1] = True

    answer = 0
    while len(queue) != 0:
        cur_pos_x, cur_pos_y, cur_hp = queue.popleft()
        added = False
        # 갈 수 있는 곳 탐색
        for idx, next_pos in enumerate(positions):
            if idx == 0:
                continue
            elif not visited[idx]:
                next_pos_x, next_pos_y, next_hp = next_pos
                # 갈 수 있는지 검사
                if ((cur_pos_x - next_pos_x) ** 2 + (cur_pos_y - next_pos_y) ** 2) <= r ** 2:
                    visited[idx] = True
                    print("--------------")
                    print(next_pos_x, next_pos_y)
                    print("--------------")
                    queue.append([next_pos_x, next_pos_y, next_hp if cur_hp == -1 else next_hp + cur_hp / 2])
                    added = True
        if not added:
            print(cur_hp, cur_pos_x, cur_pos_y)
            answer += cur_hp
    print(round(answer, 2))
if __name__ == '__main__':
    main()



