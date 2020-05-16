from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    candy_map = [list(map(int, stdin.readline().split())) for _ in range(n)]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + candy_map[i - 1][j - 1]

    print(dp[n][m])

if __name__ == "__main__":
    main()