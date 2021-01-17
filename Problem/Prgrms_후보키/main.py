def select_columns(total_columns, choose_number, visited, cur_col, candidate_keys, column_list, temp):
    visited[cur_col] = True
    temp.append(cur_col)

    for next_col in range(cur_col + 1, total_columns):
        if ''.join(map(str, temp)) in candidate_keys or str(next_col) in candidate_keys:
            continue
        if not visited[next_col] and len(temp) < choose_number:
            select_columns(total_columns, choose_number, visited, next_col, candidate_keys, column_list, temp)

    if len(temp) == choose_number:
        column_list.append(temp[:])
    temp.pop()
    visited[cur_col] = False


def check_is_candidate_key(relations, col_list, candidate_keys):
    for cols in col_list:
        tuple_set = set()
        for relations_row in range(len(relations)):
            temp = ""
            for col_num in cols:
                temp += relations[relations_row][col_num]
            tuple_set.add(temp)

        if len(tuple_set) == len(relations):
            candidate_keys.add(''.join(map(str, cols)))


def solution(relations):
    num_of_attr = len(relations[0])

    visited = [False] * num_of_attr
    candidate_keys = set()
    for choose_number in range(1, num_of_attr + 1):
        col_list = []
        for col in range(num_of_attr):
            print(candidate_keys)
            if str(col) not in candidate_keys:
                select_columns(num_of_attr, choose_number, visited, col, candidate_keys, col_list, [])
                check_is_candidate_key(relations, col_list, candidate_keys)
        # print(col_list)
    return len(candidate_keys)


print(solution([["100", "ryan", "music", "2", "a"], ["200", "apeach", "math", "2", "b"], ["300", "tube", "computer", "3", "c"],
                ["400", "con", "computer", "4", "d"], ["500", "muzi", "music", "3", "e"], ["600", "apeach", "music", "2", "f"]]))
