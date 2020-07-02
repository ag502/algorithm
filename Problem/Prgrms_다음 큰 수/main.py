from collections import Counter

def is_same_1_digit(n1, n2):
    bin_n1 = Counter(bin(n1)[2:])
    bin_n2 = Counter(bin(n2)[2:])

    if bin_n1['1'] == bin_n2['1']:
        return True
    return False

def solution(n):
    answer = 0
    next_number = n + 1
    while True:
        if is_same_1_digit(n, next_number):
            answer = next_number
            break
        next_number += 1

    return answer