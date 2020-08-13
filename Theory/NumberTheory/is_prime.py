"""
    소수판별
    많은 수 판별에는 부적합 -> 에라토스테네스의 체 사용
    시간 복잡도는 O(sqrt(n))
"""


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


print(is_prime(5))
