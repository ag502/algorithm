def solution(participants, completions):
    answer = ''
    participants.sort()
    completions.sort()

    for participant, completion in zip(participants, completions):
        if participant != completion:
            answer = participant
            break
    else:
        answer = participants(len(participants) - 1)

    return answer
