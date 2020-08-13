"""
    에라토스테네스의 체
    지워지지 않은 수들을 순회 하면서 이 수의 배수들을 지움
"""


def erathosthenes(n):
    prime_list = [i for i in range(n + 1)]

    for i in range(2, int(n ** 0.5) + 1):
        if prime_list[i] != -1:
            for j in range(i * i, n + 1, i):
                prime_list[j] = -1
    print(prime_list)


erathosthenes(21)
