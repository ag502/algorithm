from sys import stdin

def main():
    test_case = int(stdin.readline())
    dp = [[0, 0] for _ in range(41)]
    dp[0] = [1, 0]
    dp[1] = [0, 1]

    for _ in range(test_case):
        n = int(stdin.readline())

        for i in range(2, n + 1):
            dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i -2][1]]

        print('{} {}'.format(dp[n][0], dp[n][1]))

if __name__ == "__main__":
    main()