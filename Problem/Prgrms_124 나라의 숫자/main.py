num_list = [1, 2, 4]

def get_124_number(n):
    if n == 1 or n == 2 or n == 3:
        return str(num_list[n - 1])
    q = n % 3
    n = n // 3
    if q == 0:
        n -= 1
        q = 4

    return get_124_number(n) + str(q)

def solution(n):
    answer = get_124_number(n)
    return answer