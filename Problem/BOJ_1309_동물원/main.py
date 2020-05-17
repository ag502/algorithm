from sys import stdin

def main():
    n = int(stdin.readline())
    dp = [[0] * 3 for _ in range(n)]
    
    for i in range(n):
        for j in range(3):
            if i == 0:
                dp[i][j] = 1
            elif j == 0:
                dp[i][j] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
            elif j == 1:
                dp[i][j] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
            elif j== 2:
                dp[i][j] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

    print(sum(dp[n - 1]) % 9901)

if __name__ == "__main__":
    main()