from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)

moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

stdin = open("./input.txt", "r")
N, L, R = map(int, stdin.readline().split())

countries = []
for _ in range(N):
    rows = list(map(int, stdin.readline().split()))
    countries.append(rows)


def dfs(cur_row, cur_col, visited, answer):
    visited[cur_row][cur_col] = True
    answer.append((cur_row, cur_col, countries[cur_row][cur_col]))

    for moving_row, moving_col in moving_dir:
        next_row = cur_row + moving_row
        next_col = cur_col + moving_col
        if 0 <= next_row < N and 0 <= next_col < N:
            if not visited[next_row][next_col] and L <= abs(countries[cur_row][cur_col] - countries[next_row][next_col]) <= R:
                dfs(next_row, next_col, visited, answer)


def moving_people(territory):
    for area in territory:
        sum_of_people = 0
        for row, col, people in area:
            sum_of_people += people
        for row, col, _ in area:
            countries[row][col] = sum_of_people // len(area)


def main():
    count = 0
    while True:
        count += 1
        territory = []
        visited = [[False] * N for _ in range(N)]
        for row in range(N):
            for col in range(N):
                if not visited[row][col]:
                    temp = []
                    dfs(row, col, visited, temp)
                    if len(temp) <= 1:
                        continue
                    territory.append(temp)
        if len(territory) == 0:
            break
        moving_people(territory)

    print(count - 1)


if __name__ == '__main__':
    main()