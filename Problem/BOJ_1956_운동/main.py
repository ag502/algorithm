from sys import stdin, maxsize

stdin = open("./input.txt", "r")

num_of_vertex, num_of_edge = map(int, stdin.readline().split())

paths = [[float("INF")] * (num_of_vertex + 1) for _ in range(num_of_vertex + 1)]

for i in range(num_of_vertex + 1):
    paths[i][i] = 0

for _ in range(num_of_edge):
    start, end, cost = map(int, stdin.readline().split())
    paths[start][end] = min(paths[start][end], cost)


def main():
    for k in range(num_of_vertex + 1):
        for i in range(num_of_vertex + 1):
            if paths[i][k] == float("INF"):
                continue
            for j in range(num_of_vertex + 1):
                paths[i][j] = min(paths[i][k] + paths[k][j], paths[i][j])

    answer = maxsize
    for city1 in range(1, num_of_vertex + 1):
        for city2 in range(city1 + 1, num_of_vertex + 1):
            answer = min(answer, paths[city1][city2] + paths[city2][city1])

    print(-1 if answer == maxsize else answer)


if __name__ == '__main__':
    main()