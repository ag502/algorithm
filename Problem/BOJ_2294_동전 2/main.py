from sys import stdin

max_target = 100000


def main():
    stdin = open("./input.txt", "r")
    num_of_coins, target_money = map(int, stdin.readline().split())
    coins = []

    for _ in range(num_of_coins):
        coins.append(int(stdin.readline()))
    coins.sort()

    dp = [0] * (max_target + 1)
    for coin in coins:
        dp[coin] = 1

    for idx in range(1, max_target + 1):
        if dp[idx] == 1:
            continue
        for coin in coins:
            if coin > idx:
                break
            if idx > coin and dp[idx - coin] != 0:
                if dp[idx] == 0:
                    dp[idx] = dp[idx - coin] + 1
                else:
                    dp[idx] = min(dp[idx], dp[idx - coin] + 1)

    print(dp[target_money] if dp[target_money] != 0 else -1)


if __name__ == '__main__':
    main()