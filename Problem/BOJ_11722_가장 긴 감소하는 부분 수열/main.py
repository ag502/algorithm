from sys import stdin


def main():
    length_of_array = int(stdin.readline())
    numbers = list(map(int, stdin.readline().split()))
    dp = [1] * length_of_array

    for i in range(1, length_of_array):
        for j in range(i):
            if numbers[i] < numbers[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


if __name__ == "__main__":
    main()
