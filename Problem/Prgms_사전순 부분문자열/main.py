from collections import deque


def solution(s):
    answer = ''
    queue = deque()
    for word in s:
        try:
            while word > queue[0]:
                queue.popleft()
            queue.appendleft(word)
        except IndexError:
            queue.appendleft(word)

    while queue:
        answer += queue.pop()

    return answer
