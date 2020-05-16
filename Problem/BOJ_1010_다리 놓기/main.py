from sys import stdin

def main():
    test_case = int(stdin.readline())
    dp = [[0] * 30 for _ in range(30)]

    for _ in range(test_case):
        n, m = map(int, stdin.readline().split())

        for i in range(1, n + 1):
            for j in range(i, m + 1):
                if i == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = sum(dp[i - 1][j:])
        print(sum(dp[n]))

if __name__ == "__main__":
    main()