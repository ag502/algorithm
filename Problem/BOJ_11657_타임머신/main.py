from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    city_map = {}
    upper = [float('inf')] * (n + 1)
    updated = False

    upper[1] = 0

    for i in range(1, n + 1):
        city_map[i] = []

    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        city_map[a].append([b, c])

    for _ in range(n):
        updated = False
        for cur_city in range(1, n + 1):
            for next_city, time in city_map[cur_city]:
                if upper[cur_city] + time < upper[next_city]:
                    upper[next_city] = upper[cur_city] + time
                    updated = True
        if not updated:
            break
    if updated:
        upper = []

    if len(upper) == 0:
        print(-1)
    else:
        for min_distance in upper[2:]:
            if min_distance != float('inf'):
                print(min_distance)
            else:
                print(-1)

if __name__ == '__main__':
    main()


