def solution(n, words):
    answer = []

    temp = []
    if len(words[0]) == 0:
        answer = [1, 1]
        return answer
    else:
        temp.append(words[0])
    for i in range(1, len(words)):
        if words[i]  not in temp \
            and len(words[i]) != 1 \
            and words[i - 1][-1] == words[i][0]:
            temp.append(words[i])
            continue
        else:
            answer.append(n if (i + 1) % n == 0 else (i + 1) % n)
            answer.append((i + 1) // n if (i + 1) % n == 0 else (i + 1) // n + 1)

    if len(answer) == 0:
        answer = [0, 0]

    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))