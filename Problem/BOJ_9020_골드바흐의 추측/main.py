from sys import stdin
from heapq import heappush, heappop


def main():
    prime_list = [i for i in range(10001)]

    for i in range(2, int(10000 ** 0.5) + 1):
        for j in range(i * i, 10000, i):
            prime_list[j] = -1

    test_case = int(stdin.readline().rstrip())
    for _ in range(test_case):
        N = int(stdin.readline().rstrip())

        prime_subtract = []

        for idx in range(2, N):
            cur_number = prime_list[idx]
            if cur_number != -1:
                target = N - cur_number
                if target >= cur_number and prime_list[target] != -1:
                    heappush(prime_subtract, (target -
                                              cur_number, cur_number, target))

        prime_info = heappop(prime_subtract)
        print(str(prime_info[1]) + " " + str(prime_info[2]))


if __name__ == "__main__":
    main()
