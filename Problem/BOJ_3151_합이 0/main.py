from sys import stdin

stdin = open("./input.txt", "r")
num_of_student = int(stdin.readline())
ability = list(map(int, stdin.readline().split()))
ability.sort()


def lower_bound(start_idx, target):
    left_ptr = start_idx
    right_ptr = len(ability)

    while left_ptr < right_ptr:
        mid = (left_ptr + right_ptr) // 2
        if ability[mid] >= target:
            right_ptr = mid
        else:
            left_ptr = mid + 1

    return right_ptr


def upper_bound(start_idx, target):
    left_ptr = start_idx
    right_ptr = len(ability)

    while left_ptr < right_ptr:
        mid = (left_ptr + right_ptr) // 2
        if ability[mid] > target:
            right_ptr = mid
        else:
            left_ptr = mid + 1
    return right_ptr


def main():
    answer = 0
    for first_student in range(len(ability) - 2):
        for second_student in range(first_student + 1, len(ability) - 1):
            sum_of_ability = ability[first_student] + ability[second_student]
            idx_1 = lower_bound(second_student + 1, -sum_of_ability)
            idx_2 = upper_bound(second_student + 1, -sum_of_ability)

            answer += (idx_2 - idx_1)
    print(answer)


if __name__ == '__main__':
    main()