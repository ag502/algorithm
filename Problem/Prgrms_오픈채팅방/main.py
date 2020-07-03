nick_name = {}

def process_query(query_string):
    query_list = query_string.split()

    action = query_list[0]
    uid = query_list[1]

    if action == 'Enter':
        nick_name[uid] = query_list[2]
        return (uid, '님이 들어왔습니다.')
    elif action == 'Leave':
        return (uid, '님이 나갔습니다.')
    elif action == 'Change':
        nick_name[uid] = query_list[2]
        return None

def solution(records):
    answer = []
    for record in records:
        result = process_query(record)
        if result is None:
            continue
        answer.append(result)

    for idx, result in enumerate(answer):
        answer[idx] = nick_name[result[0]] + result[1]

    return answer