from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

moving = [
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
    [-1, 0],
    [-1, 1],
]

def main():
    while True:
        w, h = map(int, stdin.readline().split())
        if w == 0 and h == 0:
            return

        island_map = []
        visited = []
        for _ in range(h):
            row = list(map(int, stdin.readline().split()))
            island_map.append(row)
            visited.append([0] * len(row))

        answer = 0
        for i in range(h):
            for j in range(w):
                if island_map[i][j] != 0 and visited[i][j] != -1:
                    search_map(island_map, visited, i, j, w, h)
                    answer += 1

        print(answer)

def search_map(island_map, visited, start_row, start_col, w, h):
    # 1. 체크인
    visited[start_row][start_col] = -1
    # 2. 도착?
    # 3. 갈 수 있는 인접 섬 탐색
    for x, y in moving:
        # 4. 갈 수 있는지 검사
        moving_x = start_col + x
        moving_y = start_row + y
        if 0 <= moving_x < w and 0 <= moving_y < h \
                and island_map[moving_y][moving_x] != 0\
                and visited[moving_y][moving_x] == 0:
            # 5. 간다
            search_map(island_map, visited, moving_y, moving_x, w, h)

if __name__ == '__main__':
    main()