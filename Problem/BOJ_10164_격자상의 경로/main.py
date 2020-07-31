from sys import stdin


def main():
    row, column, mark = map(int, stdin.readline().split())
    dp = [[0] * (column + 1) for _ in range(row + 1)]
    dp[1][1] = 1

    total_case = 0
    dp_temp = dp[:]
    for i in range(1, row + 1):
        for j in range(1, column + 1):
            if i == 1 and j == 1:
                continue
            dp_temp[i][j] = dp_temp[i][j - 1] + dp_temp[i - 1][j]
    total_case = dp_temp[row][column]

    dp[(mark - 1) // column + 1][(mark - 1) % column + 1] = -1
    except_case = 0
    if mark != 0:
        for i in range(1, row + 1):
            for j in range(1, column + 1):
                if i == 1 and j == 1:
                    continue
                if dp[i][j] == -1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        except_case = dp[row][column]

    print(total_case - except_case)


if __name__ == "__main__":
    main()
