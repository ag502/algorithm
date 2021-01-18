def check_candidate_key(relations, keys):
    tuple_set = set()
    rows = len(relations)
    for row in range(rows):
        temp_string = ""
        for key in keys:
            temp_string += relations[row][key]
        tuple_set.add(temp_string)

    if len(tuple_set) == rows:
        return True
    return False


def dfs(relations, num_of_attr, cur_key, key_temp, candidate_keys):
    key_temp.append(cur_key)

    if not check_candidate_key(relations, key_temp):
        for next_key in range(cur_key + 1, num_of_attr):
            dfs(relations, num_of_attr, next_key, key_temp, candidate_keys)
    else:
        candidate_keys.append(set(key_temp[:]))
    key_temp.pop()


def solution(relations):
    num_of_attributes = len(relations[0])

    candidate_keys = []

    for attr in range(num_of_attributes):
        dfs(relations, num_of_attributes, attr, [], candidate_keys)

    candidate_keys.sort(key=lambda x: len(x))

    # print(candidate_keys)

    answer = []
    for i in range(len(candidate_keys) - 1):
        if candidate_keys[i] == -1:
            continue
        else:
            answer.append(candidate_keys[i])
        for j in range(i + 1, len(candidate_keys)):
            if candidate_keys[j] != -1:
                intersection = candidate_keys[i] & candidate_keys[j]
                if len(intersection) == len(candidate_keys[i]):
                    candidate_keys[j] = -1
    if candidate_keys[len(candidate_keys) - 1] != -1:
        answer.append(candidate_keys[len(candidate_keys) - 1])

    return len(answer)


print(solution(
    [["100", "ryan", "music", "2", "a"], ["200", "apeach", "math", "2", "b"], ["300", "tube", "computer", "3", "c"],
     ["400", "con", "computer", "4", "d"], ["500", "muzi", "music", "3", "e"], ["600", "apeach", "music", "2", "f"]]))
