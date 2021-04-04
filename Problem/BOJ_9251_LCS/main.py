from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    string1 = stdin.readline().rstrip()
    string2 = stdin.readline().rstrip()

    dp = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

    for string1_idx in range(1, len(string1) + 1):
        for string2_idx in range(1, len(string2) + 1):
            if string1[string1_idx - 1] == string2[string2_idx - 1]:
                dp[string1_idx][string2_idx] = dp[string1_idx - 1][string2_idx - 1] + 1
            else:
                dp[string1_idx][string2_idx] = max(dp[string1_idx - 1][string2_idx], dp[string1_idx][string2_idx - 1])

    # print(dp)
    answer = 0
    for row in dp:
        answer = max(answer, max(row))

    print(answer)


if __name__ == '__main__':
    main()