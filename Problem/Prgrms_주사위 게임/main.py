from itertools import product


def solution(monster, S1, S2, S3):
    moving_num = [i - 1 for i in monster]
    total_case = S1 * S2 * S3
    count = 0
    for dice_num in product(range(1, S1 + 1), range(1, S2 + 1), range(1, S3 + 1)):
        if sum(dice_num) in moving_num:
            count += 1

    answer = int(((total_case - count) / total_case) * 1000)

    return answer
