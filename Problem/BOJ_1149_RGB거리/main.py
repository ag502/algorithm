from sys import stdin

def main():
    n = int(stdin.readline())
    paint_cost = [list(map(int, stdin.readline().split())) for _ in range(n)]
    dp = [[0] * 3 for _ in range(n)]

    for i in range(n):
        for j in range(3):
            if i == 0:
                dp[i][j] = paint_cost[i][j]
            else:
                temp = 1000001
                for k in range(3):
                    if j != k:
                        if temp > dp[i - 1][k]:
                            temp = dp[i - 1][k]
                dp[i][j] = paint_cost[i][j] + temp
    print(min(dp[n - 1]))

if __name__ == "__main__":
    main()