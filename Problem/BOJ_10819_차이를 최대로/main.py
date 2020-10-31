from sys import stdin

def dfs(numbers, visited, cur_idx, answer, temp):
    # 1. 방문
    visited[cur_idx] = True
    # 2. 도착
    temp.append(numbers[cur_idx])
    # 3. 주면 탐색
    for next_idx in range(len(numbers)):
        # 4. 갈 수 있는지 검사
        if not visited[next_idx]:
            dfs(numbers, visited, next_idx, answer, temp)
    # 5. 체크아웃
    visited[cur_idx] = False
    if len(temp) == len(numbers):
        answer.append(temp[:])
    temp.pop()

def do_operation(numbers):
    answer = 0
    for idx in range(len(numbers) - 1):
        answer += abs(numbers[idx] - numbers[idx + 1])
    return answer

def main():
    stdin = open('./test_case.txt', 'r')
    n = int(stdin.readline())
    numbers = list(map(int, stdin.readline().split()))
    visited = [False] * len(numbers)
    answer = []
    for idx, number in enumerate(numbers):
        if not visited[idx]:
            dfs(numbers, visited, idx, answer, [])

    max_value = 0
    for numbers in answer:
        max_value = max(max_value, do_operation(numbers))
    print(max_value)

if __name__ == '__main__':
    main()