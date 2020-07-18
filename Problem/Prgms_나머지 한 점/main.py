from collections import Counter


def solution(v):
    answer = []

    x_coord, y_coord = list(zip(*v))
    x_coord = Counter(x_coord)
    y_coord = Counter(y_coord)

    for coord in x_coord.keys():
        if x_coord[coord] == 1:
            answer.append(coord)
            break

    for coord in y_coord.keys():
        if y_coord[coord] == 1:
            answer.append(coord)
            break

    return answer
