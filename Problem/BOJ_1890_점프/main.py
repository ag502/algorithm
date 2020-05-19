from sys import stdin

def main():
    n = int(stdin.readline())
    game_map = [list(map(int, stdin.readline().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if dp[i][j] == 0:
                continue
            if i == n - 1 and j == n - 1:
                break
            movable_distance = game_map[i][j]
            if movable_distance != 0:
                if i + movable_distance <= n - 1:
                    dp[i + movable_distance][j] += dp[i][j]
                if j + movable_distance <= n - 1:
                    dp[i][j + movable_distance] += dp[i][j]

    print(dp[n - 1][n - 1])

if __name__ == "__main__":
    main()

