from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    input_array = list(map(int, stdin.readline().split()))
    input_array = [0] + input_array
    input_array.sort()

    visited = [False] * (N + 1)
    for idx in range(1, N + 1):
        combination(idx, N, M, 0, input_array, visited, [])


def combination(cur_idx, n, m, selected_idx, array, visited, answer):
    # 1. 체크인
    visited[cur_idx] = True
    selected_idx += 1
    # 2. 도착
    answer.append(str(array[cur_idx]))
    # 3. 인접 노드 순회
    for next_idx in range(cur_idx + 1, n + 1):
        # 4. 갈 수 있는지 검사
        if not visited[next_idx] and selected_idx != m:
            combination(next_idx, n, m, selected_idx, array, visited, answer)
    # 5. 체크아웃
    if len(answer) == m:
        print(' '.join(answer))
    selected_idx -= 1
    answer.pop()
    visited[cur_idx] = False


if __name__ == "__main__":
    main()
