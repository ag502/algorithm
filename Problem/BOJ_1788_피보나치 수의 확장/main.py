from sys import stdin

def main():
    n = int(stdin.readline())

    dp = [0] * 1000001
    dp[0] = 0
    dp[1] = 1

    for i in range(2, abs(n) + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10 ** 9

    if n > 0:
        print(1)
    elif n == 0:
        print(0)
    else:
        print(-1 if abs(n) % 2 == 0 else 1)

    print(dp[abs(n)])

if __name__ == "__main__":
    main()