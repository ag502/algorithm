from sys import stdin


def main():
    N = int(stdin.readline())
    prime_nums = [0] * (N + 1)

    for i in range(1, len(prime_nums)):
        for j in range(i, len(prime_nums), i):
            prime_nums[j] += i
        prime_nums[i] += prime_nums[i - 1]

    print(prime_nums[N])


if __name__ == "__main__":
    main()
