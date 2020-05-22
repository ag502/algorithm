from itertools import permutations

def solution(d, budget):
    answer = 0

    for i in range(1, len(d) + 1):
        chosen_part = list(permutations(d, i))
        sum_of_budget_list = list(map(sum, chosen_part))

        if budget in sum_of_budget_list:
            answer = i

    return answer

print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))