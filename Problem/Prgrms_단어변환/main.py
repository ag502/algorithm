from collections import deque

def can_change(word_1, word_2):
    difference = 0
    for char_1, char_2 in zip(word_1, word_2):
        if char_1 != char_2:
            difference += 1
        if difference > 1:
            return False
    return True

def solution(begin, target, words):
    answer = 0
    queue = deque()
    visited = [False] * len(words)

    queue.append(begin)

    while len(queue) != 0:
        size = len(queue)
        answer += 1
        for _ in range(size):
            cur_word = queue.popleft()

            if cur_word == target:
                return answer - 1
            for idx, next_word in enumerate(words):
                if can_change(cur_word, next_word) and not visited[idx]:
                    queue.append(next_word)
                    visited[idx] = True
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))