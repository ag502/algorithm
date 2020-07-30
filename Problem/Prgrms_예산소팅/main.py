def solution(d, budget):
    answer = 0
    d.sort()
    acc_require = 0
    for require in d:
        acc_require += require
        if acc_require <= budget:
            answer += 1
        else:
            break
    return answer
