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
