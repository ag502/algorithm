num_list = [1, 2, 4]

def get_124_number(n):
    if 0 < n <= 3:
        return str(num_list[n - 1])

    p, q = divmod(n - 1, 3)
    return get_124_number(p) + str(num_list[q])

def solution(n):
    answer = get_124_number(n)
    return answer