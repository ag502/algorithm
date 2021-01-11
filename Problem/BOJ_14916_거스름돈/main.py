from sys import stdin, maxsize


def main():
    stdin = open('./input.txt', 'r')
    change = int(stdin.readline())

    dp = [maxsize] * 100001
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1

    for cur_change in range(6, change + 1):
        dp[cur_change] = min(dp[cur_change - 2], dp[cur_change - 5]) + 1

    print(dp[change] if dp[change] <= 50000 else -1)


if __name__ == '__main__':
    main()