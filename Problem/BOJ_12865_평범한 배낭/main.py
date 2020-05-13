from sys import stdin

def main():
    n, k = list(map(int, stdin.readline().split()))
    cache = [[0] * (k + 1) for _ in range(0, n + 1)]

    bag_objects = []
    for i in range(n):
        w, v = list(map(int, stdin.readline().split()))
        bag_objects.append((w, v))

    for i in range(len(bag_objects)):
        for max_weight in range(1, k + 1):
            if max_weight < bag_objects[i][0]:
                cache[i + 1][max_weight] = cache[i][max_weight]
                continue
            cache[i + 1][max_weight] = max(cache[i][max_weight], cache[i][max_weight - bag_objects[i][0]] + bag_objects[i][1])
    print(cache[n][k])

if __name__ == "__main__":
    main()