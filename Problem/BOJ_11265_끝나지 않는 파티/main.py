from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    graph = [[0] * (n + 1)]
    for _ in range(n):
        graph.append([0] + list(map(int, stdin.readline().split())))

    # Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        if graph[a][b] <= c:
            print("Enjoy other party")
        else:
            print("Stay here")

if __name__ == '__main__':
    main()