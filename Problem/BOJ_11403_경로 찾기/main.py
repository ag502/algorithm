from sys import stdin

def main():
    vertex = int(stdin.readline())
    graph = []

    for _ in range(vertex):
        row = list(map(int, stdin.readline().split()))
        graph.append(row)

    # Floyd-Warshall
    for k in range(vertex):
        for i in range(vertex):
            if graph[i][k] == 0:
                continue
            for j in range(vertex):
                graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])

    for row in graph:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    main()