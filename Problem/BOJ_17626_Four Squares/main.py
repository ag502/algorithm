from sys import stdin, maxsize


def main():
    stdin = open("./input.txt", "r")
    number = int(stdin.readline())

    dp = [maxsize] * (number + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(2, int(number ** 0.5) + 1):
        dp[i * i] = 1

    for number in range(3, number + 1):
        for i in range(1, int(number ** 0.5) + 1):
            dp[number] = min(dp[number], dp[i * i] + dp[number - i * i])

    print(dp[number])


if __name__ == '__main__':
    main()