from sys import stdin


def get_last_char(word):
    return word[len(word) - 1]


def get_first_char(word):
    return word[0]


def last_word_game(words, visited, cur_idx, num_of_words, spoke_word):
    # 1. 방문
    visited[cur_idx] = True
    spoke_word.append(words[cur_idx])
    # 2. 가능한 주변 탐색
    for next_idx in range(num_of_words):
        # 3. 갈 수 있는지 검사
        if not visited[next_idx] and get_last_char(words[cur_idx]) == get_first_char(words[next_idx]):
            # 4. 간다
            return last_word_game(words, visited, next_idx, num_of_words, spoke_word)
    # 5. 체크아웃
    visited[cur_idx] = False
    if len(spoke_word) == num_of_words:
        return 1
    return 0


def main():
    stdin = open('./input.txt', 'r')
    num_of_words = int(stdin.readline())
    words = list(stdin.readline().split())

    for idx in range(num_of_words):
        visited = [False] * num_of_words
        answer = last_word_game(words, visited, idx, num_of_words, [])
        if answer == 1:
            print(answer)
            return
    print(0)


if __name__ == '__main__':
    main()