from sys import stdin

MAX_WEIGHT = 100000


def main():
    stdin = open("./input.txt", "r")
    num_of_items, target_weight = map(int, stdin.readline().split())
    items = [(0, 0)]

    for _ in range(num_of_items):
        items.append(tuple(map(int, stdin.readline().split())))
    items.sort(key=lambda x: (x[0], x[1]))

    dp = [[0] * (target_weight + 1) for _ in range(num_of_items + 1)]

    for num_of_item in range(1, num_of_items + 1):
        for weight in range(1, target_weight + 1):
            temp = 0
            if weight >= items[num_of_item][0]:
                temp = dp[num_of_item - 1][weight - items[num_of_item][0]] + items[num_of_item][1]
            dp[num_of_item][weight] = max(dp[num_of_item - 1][weight], temp)

    print(dp[num_of_item][weight])


if __name__ == '__main__':
    main()