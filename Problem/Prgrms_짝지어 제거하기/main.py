from collections import deque


def solution(s):
    stack = deque()

    for alphabet in s:
        try:
            top = stack[0]
            if alphabet == top:
                stack.popleft()
            else:
                stack.appendleft(alphabet)
        except IndexError:
            stack.appendleft(alphabet)

    if not stack:
        return 1
    return 0
