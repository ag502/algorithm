from sys import stdin, maxsize
from heapq import heappush, heappop

stdin = open("./input.txt", "r")
num_of_cities = int(stdin.readline())
weights = []
for _ in range(num_of_cities):
    weights.append(list(map(int, stdin.readline().split())))

cities = {}
for city in range(num_of_cities):
    cities[city] = []

for row in range(num_of_cities):
    for col in range(num_of_cities):
        if weights[row][col] != 0:
            cities[row].append(col)

min_cost = maxsize
paths = []
visited = [False] * num_of_cities


def dfs(cur_city, sum, count):
    global min_cost
    visited[cur_city] = True
    count += 1
    for next_city in cities[cur_city]:
        if not visited[next_city] and sum < min_cost:
            dfs(next_city, sum + weights[cur_city][next_city], count)

    if count == num_of_cities:
        if weights[cur_city][0] != 0:
            min_cost = min(min_cost, sum + weights[cur_city][0])
    visited[cur_city] = False


def main():
    dfs(0, 0, 0)
    print(min_cost)


if __name__ == '__main__':
    main()