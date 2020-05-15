from sys import stdin

def main():
    n, k = map(int, stdin.readline().split())
    # upper = 1
    # below = 1
    #
    # for i in range(0, k):
    #     upper *= (n - i)
    # for i in range(1, k + 1):
    #     below *= i
    # print((upper // below) % 10007)

    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(0, k + 1):
        for j in range(i, n + 1):
            if i == 0:
                dp[i][j] = 1
            elif i == 1:
                dp[i][j] = j
            else:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % 10007

    print(dp[k][n])

if __name__ == "__main__":
    main()