from sys import stdin, setrecursionlimit

def permutation(n, cur_number, visited, answer, temp):
    # 1. 방문
    visited[cur_number] = True
    # 2. 도착
    temp.append(cur_number)
    # 3. 탐색
    for next_number in range(10):
        if not visited[next_number] and len(temp) < n:
            permutation(n, next_number, visited, answer, temp)
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
    answer = []
    for number in range(10):
        permutation(len(alphabets), number, visited, answer, [])

    # print(answer)
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