from sys import stdin


def main():
    prime_nums = [0] * (int(1e6) + 1)
    for i in range(1, len(prime_nums)):
        for j in range(i, len(prime_nums), i):
            prime_nums[j] += i
        prime_nums[i] += prime_nums[i - 1]

    TEST_CASE = int(stdin.readline())

    for _ in range(TEST_CASE):
        N = int(stdin.readline())
        print(prime_nums[N])


if __name__ == "__main__":
    main()
