from sys import stdin

def main():
    stdin = open("Problem/BOJ_12865_평범한 배낭/input.txt", "r")
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
    
    for row in cache:
        print(row)

if __name__ == "__main__":
    main()