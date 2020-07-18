from collections import deque


def solution(max_weight, specs, names):
    answer = 1
    specs = dict(specs)
    names = deque(names)

    current_weight = 0
    while names:
        weight = int(specs[names.popleft()])
        if max_weight < current_weight + weight:
            answer += 1
            current_weight = weight
        else:
            current_weight += weight

    return answer
