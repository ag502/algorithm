from sys import stdin


def floyd_warshall(bus_path, num_of_city):
    for k in range(1, num_of_city + 1):
        for i in range(1, num_of_city + 1):
            if bus_path[i][k] == float("INF"):
                continue
            for j in range(1, num_of_city + 1):
                bus_path[i][j] = min(bus_path[i][k] + bus_path[k][j], bus_path[i][j])


def main():
    stdin = open("./input.txt", "r")
    num_of_cities = int(stdin.readline())
    num_of_bus = int(stdin.readline())

    bus_path = [[float("INF")] * (num_of_cities + 1) for _ in range(num_of_cities + 1)]
    for i in range(num_of_cities + 1):
        bus_path[i][i] = 0

    for _ in range(num_of_bus):
        start, end, cost = map(int, stdin.readline().split())
        bus_path[start][end] = min(bus_path[start][end], cost)

    floyd_warshall(bus_path, num_of_cities)

    for row in bus_path[1:]:
        temp = []
        for cost in row[1:]:
            if cost == float("INF"):
                temp.append("0")
            else:
                temp.append(str(cost))
        print(' '.join(temp))


if __name__ == '__main__':
    main()