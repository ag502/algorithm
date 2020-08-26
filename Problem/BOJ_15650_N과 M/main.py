from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    visited = [False] * (N + 1)
    for i in range(1, N + 1):
        combination(i, N, M, 0, visited, [])


def combination(cur_num, n, m, selected_num, visited, answer):
    # 1. 체크인
    visited[cur_num] = True
    selected_num += 1
    # 2. 도착
    answer.append(str(cur_num))
    # 3. 인접 노드 순회
    for next_num in range(cur_num + 1, n + 1):
        # 4. 갈 수 있는지 검사
        if not visited[next_num] and selected_num != m:
            combination(next_num, n, m, selected_num, visited, answer)
    # 5. 체크아웃
    if len(answer) == m:
        print(' '.join(answer))
    answer.pop()
    visited[cur_num] = False
    selected_num -= 1


if __name__ == "__main__":
    main()
