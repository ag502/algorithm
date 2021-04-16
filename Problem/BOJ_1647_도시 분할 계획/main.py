from sys import stdin

stdin = open("./input.txt", "r")
num_of_house, num_of_relation = map(int, stdin.readline().split())
edges = []

for _ in range(num_of_relation):
    house_1, house_2, cost = map(int, stdin.readline().split())
    edges.append((house_1, house_2, cost))

edges.sort(key=lambda x: x[2])
parents = [i for i in range(num_of_house + 1)]


def find(house):
    if house == parents[house]:
        return house
    parents[house] = find(parents[house])
    return parents[house]


def merge(home_1, home_2):
    home_1_parent = find(home_1)
    home_2_parent = find(home_2)
    if home_1_parent == home_2_parent:
        return
    parents[home_2_parent] = home_1_parent


def main():
    answer = 0
    cost_list = []
    for home_1, home_2, edge_cost in edges:
        if find(home_1) == find(home_2):
            continue
        cost_list.append(edge_cost)
        merge(home_1, home_2)
        answer += edge_cost

    print(answer - max(cost_list))


if __name__ == '__main__':
    main()