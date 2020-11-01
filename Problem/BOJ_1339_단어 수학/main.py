from sys import stdin

def permutation(n, numbers, cur_idx, visited, answer, temp):
    # 1. 방문
    cur_number = numbers[cur_idx]
    visited[cur_number] = True
    # 2. 도착
    temp.append(cur_number)
    # 3. 탐색
    for next_idx in range(len(numbers)):
        next_number = numbers[next_idx]
        if not visited[next_number] and len(temp) < n:
            permutation(n, numbers, next_idx, visited, answer, temp)
    # 4. 체크아웃
    visited[cur_number] = False
    if len(temp) == n:
        # answer.append(temp[:])
        answer.append(''.join(map(str, temp)))
    temp.pop()

def main():
    stdin = open('./test_case.txt', 'r')
    n = int(stdin.readline())
    words = []
    alphabets = set()

    for _ in range(n):
        word = stdin.readline().rstrip()
        words.append(word)
        for char in word:
            alphabets.add(char)

    visited = [False] * 10
    alphabets = list(alphabets)
    numbers = [i for i in range(9, 9 - len(alphabets), -1)]
    answer = []

    for idx in range(len(numbers)):
        permutation(len(alphabets), numbers, idx, visited, answer, [])

    max_value = -1
    for num_list in answer:
        table = {}
        sum = 0
        for num, char in zip(num_list, alphabets):
            table[char] = str(num)
        for word in words:
            char_num = ""
            for char in word:
                char_num += table[char]
            sum += int(char_num)
        max_value = max(max_value, sum)
    print(max_value)


if __name__ == '__main__':
    main()