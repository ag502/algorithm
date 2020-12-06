from sys import stdin

def main():
    stdin = open('./input.txt', 'r')
    n, m = map(int, stdin.readline().split())

    stop_by = []
    for _ in range(m):
        stop_by.append(int(stdin.readline()) - 1)

    treasure_map = []
    for _ in range(n):
        treasure_map.append(list(map(int, stdin.readline().split())))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                treasure_map[i][j] = min(treasure_map[i][j], treasure_map[i][k] + treasure_map[k][j])

    answer = 0
    for start, end in zip(stop_by, stop_by[1:]):
        answer += treasure_map[start][end]

    print(answer)

if __name__ == '__main__':
    main()