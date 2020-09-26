from sys import stdin, setrecursionlimit

setrecursionlimit(10000)

direction_row = [1, -1, 0, 0]
direction_col = [0, 0, 1, -1]

def main():
    test_case = int(stdin.readline())
    for _ in range(test_case):
        answer = 0
        cols, rows, k = map(int, stdin.readline().split())
        field = {}
        for i in range(rows):
            field[i] = []
        visited = [[0] * cols for _ in range(rows)]

        for _ in range(k):
            col, row = map(int, stdin.readline().split())
            field[row].append(col)

        for i in range(rows):
            for j in range(cols):
                if visited[i][j] != -1 and j in field[i]:
                    dfs(field, visited, i, j, cols, rows)
                    answer += 1
        print(answer)

def dfs(field, visited, start_row, start_col, cols, rows):
    # 1. 방문
    visited[start_row][start_col] = -1
    # 2. 목적지?
    # 3. 갈 수 있는 인접노드 탐색
    for row, col in zip(direction_row, direction_col):
        can_go_row = start_row + row
        can_go_col = start_col + col
        if 0 <= can_go_row < rows and 0 <= can_go_col < cols:
            # 4. 갈 수 있는지 검사
            if visited[can_go_row][can_go_col] != -1 and can_go_col in field[can_go_row]:
                # 5. 간다
                dfs(field, visited, can_go_row, can_go_col, cols, rows)

if __name__ == '__main__':
    main()