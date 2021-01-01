from sys import stdin, maxsize
from math import sqrt


def prime_sieve(number):
    primes = [i for i in range(number + 1)]
    for i in range(2, int(number ** 0.5) + 1):
        for j in range(i * i, number + 1, i):
            if primes[j] != -1:
                primes[j] = -1
    return primes


def main():
    stdin = open('./input.txt', 'r')
    test_case = int(stdin.readline())
    primes = prime_sieve(100000)[2:]

    temp = []
    for num in primes:
        if num != -1:
            temp.append(num)

    for _ in range(test_case):
        target = int(stdin.readline())
        result = maxsize

        start = 0
        end = len(temp) - 1
        while start < end:
            temp_result = temp[start] * temp[end]
            if temp_result >= target:
                result = min(result, temp_result)

            if temp_result < target:
                start += 1
            else:
                end -= 1
        print(result)


if __name__ == '__main__':
    main()