from sys import stdin

def find(parents, city):
    if parents[city] == city:
        return city
    parents[city] = find(parents, parents[city])
    return parents[city]

def merge(parents, city1, city2):
    city1_root = find(parents, city1)
    city2_root = find(parents, city2)
    if city1_root == city2_root:
        return
    parents[city2_root] = city1_root

def main():
    stdin = open('./test_case.txt', 'r')
    num_of_cities = int(stdin.readline())
    num_of_travel_cities = int(stdin.readline())

    city_map = []
    for _ in range(num_of_cities):
        row = list(map(int, stdin.readline().split()))
        city_map.append(row)
    travel_cities = list(map(int, stdin.readline().split()))
    parents = [i for i in range(num_of_cities)]

    for city1 in range(len(city_map)):
        for city2 in range(len(city_map)):
            if city_map[city1][city2] == 1:
                merge(parents, city1, city2)

    root = find(parents, travel_cities[0] - 1)
    for city in travel_cities:
        if root != find(parents, city - 1):
            print('NO')
            return
    print('YES')

if __name__ == '__main__':
    main()