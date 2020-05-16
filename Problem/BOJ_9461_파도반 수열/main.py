from sys import stdin

def main():
    test_case = int(input())

    for _ in range(test_case):
        n = int(input())
        dp = [1, 1, 1, 2, 2] + [0] * (n - 5)

        for i in range(5, n):
            dp[i] = dp[i - 1] + dp[i - 5]

        print(dp[n - 1])

if __name__ == "__main__":
    main()