from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    num_of_cards = int(stdin.readline())
    cards_cost = [0] + list(map(int, stdin.readline().split()))

    dp = [0] * (num_of_cards + 1)
    dp[1] = cards_cost[1]

    for idx in range(2, num_of_cards + 1):
        for num_of_card in range(1, idx // 2 + 1):
            dp[idx] = max(cards_cost[idx], dp[idx], dp[num_of_card] + dp[idx - num_of_card])

    print(dp[num_of_cards])


if __name__ == '__main__':
    main()