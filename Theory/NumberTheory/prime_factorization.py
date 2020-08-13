"""
    소인수 분해
    합성수를 소수인 인수의 곱으로 표현
"""

from collections import deque


def prime_factorization(n):
    prime_factor = deque()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n = n // i
            prime_factor.append(i)
    if n > 1:
        prime_factor.append(n)

    print(prime_factor)


prime_factorization(46)

"""
    에라토스테네스의 체를 이용한 소인수 분해
    합성수인 경우 1을 제외한 약수 중 가장 작은 약수의 정보를 저장해 놓음
"""


def prime_factorization_sieve(n):
    prime_list = [i for i in range(n + 1)]
    prime_list[0] = prime_list[1] = -1

    for i in range(2, int(n ** 0.5) + 1):
        if prime_list[i] == i:
            for j in range(i * i, n + 1, i):
                if prime_list[j] == j:
                    prime_list[j] = i

    return prime_list


def prime_factorization2(n):
    prime_factor = deque()
    prime_list = prime_factorization_sieve(n)

    while n > 1:
        prime_factor.append(prime_list[n])
        n //= prime_list[n]

    print(prime_factor)


prime_factorization2(46)
