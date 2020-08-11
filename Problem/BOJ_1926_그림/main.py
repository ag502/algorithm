from sys import stdin


def main():
    # 세로: n, 가로: m
    n, m = map(int, stdin.readline().split())
    canvas = [list(map(int, stdin.readline().split())) for _ in range(n)]

    is_visited = [-1] * n

    answer = 0
    # for i in range(n):
    dfs(0, canvas, is_visited, answer)

    print(is_visited)
    print(answer)


def dfs(start_point, matrix, is_visited, answer):
    # 1. 체크인
    is_visited[start_point] = 0
    # 2. 목적지?
    print(start_point)
    answer += 1
    # print(answer)
    # 3. 갈 수 있는 곳 순회
    for idx, next_point in enumerate(matrix[start_point]):
        # 4. 갈 수 있는 곳 검사
        if next_point == 1 and is_visited[idx] == -1:
            dfs(idx, matrix, is_visited, answer)
    # 5. 체크아웃
    is_visited[start_point] = 1
    answer -= 1


if __name__ == "__main__":
    main()
