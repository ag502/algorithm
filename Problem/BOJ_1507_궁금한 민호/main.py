from sys import stdin

stdin = open("./input.txt", "r")
num_of_city = int(stdin.readline())

times = [[0] * (num_of_city + 1)]
for _ in range(num_of_city + 1):
    times.append([0] + list(map(int, stdin.readline().split())))


def main():
    city_map = [[float("INF")] * (num_of_city + 1) for _ in range(num_of_city + 1)]

    for i in range(num_of_city + 1):
        city_map[i][i] = 0

    for city1 in range(1, num_of_city + 1):
        for city2 in range(1, num_of_city + 1):
            cur_time = times[city1][city2]
            if cur_time != 0:
                for k in range(1, num_of_city + 1):
                    if k == city1 or k == city2:
                        continue
                    if cur_time == times[city1][k] + times[k][city2]:
                        break
                else:
                    city_map[city1][city2] = cur_time

    answer = 0
    for row in range(1, num_of_city + 1):
        for col in range(row + 1, num_of_city + 1):
            if city_map[row][col] != float("INF"):
                answer += city_map[row][col]

    for k in range(1, num_of_city + 1):
        for i in range(1, num_of_city + 1):
            if city_map[i][k] == float("INF"):
                continue
            for j in range(1, num_of_city + 1):
                city_map[i][j] = min(city_map[i][j], city_map[i][k] + city_map[k][j])

    for times_row, row in zip(times[1:], city_map[1:]):
        for cost1, cost2 in zip(times_row[1:], row[1:]):
            if cost1 != cost2:
                print(-1)
                return

    print(answer)


if __name__ == '__main__':
    main()