from sys import stdin


def main():
    test_case = int(stdin.readline())
    # prime_sum = [set([1, i]) for i in range(int(1e6) + 1)]
    prime_sum = [0] * (int(1e6) + 1)
    # print(prime_sum)

    # for i in range(2, int(1e6 ** 0.5) + 1):
    #     for j in range(i * 2, len(prime_sum), i):
    #         prime_sum[j].add(i)
    #         prime_sum[j].add(j // i)
    prime_sum[1] = 1
    for i in range(2, len(prime_sum)):
        prime_sum[i] = (i + 1)

    for i in range(2, int(1e6 ** 0.5) + 1):

        for j in range(i * 2, len(prime_sum), i):
            prime_sum[j] += i
            if j // i > int(1e6 ** 0.5) and j // i != i:
                prime_sum[j] += (j // i)

    # print(prime_sum)

    for _ in range(test_case):
        n = int(stdin.readline())
        acc_sum = 0
        for i in range(1, n + 1):
            # acc_sum += sum(prime_sum[i])
            acc_sum += prime_sum[i]
        print(acc_sum)


if __name__ == "__main__":
    main()
