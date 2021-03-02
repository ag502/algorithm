from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    num_of_coins, target_money = map(int, stdin.readline().split())

    coins = []
    for _ in range(num_of_coins):
        coins.append(int(stdin.readline()))
    coins.sort()

    dp = [0] * (target_money + 1)
    for coin_cost in coins:
        if coin_cost > target_money:
            break
        dp[coin_cost] += 1
        for idx in range(coin_cost + 1, target_money + 1):
            dp[idx] += dp[idx - coin_cost]

    print(dp[target_money])


if __name__ == '__main__':
    main()