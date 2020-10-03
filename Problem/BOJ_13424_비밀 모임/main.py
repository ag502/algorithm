from sys import stdin

def main():
    test_case = int(stdin.readline())
    for _ in range(test_case):
        n, m = map(int, stdin.readline().split())
        secret_map = [[float('inf')] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            secret_map[i][i] = 0

        for _ in range(m):
            a, b, c = map(int, stdin.readline().split())
            secret_map[a][b] = c
            secret_map[b][a] = c

        k = int(stdin.readline())
        rooms = list(map(int, stdin.readline().split()))
        answer = []

        # Floyd-Warshall
        for room in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    secret_map[i][j] = min(secret_map[i][j], secret_map[i][room] + secret_map[room][j])

        for i in range(1, n + 1):
            total_distance = 0
            for room in rooms:
                total_distance += secret_map[i][room]
            answer.append((i, total_distance))

        answer = sorted(answer, key=lambda x: (x[1], x[0]))
        print(answer[0][0])

if __name__ == '__main__':
    main()