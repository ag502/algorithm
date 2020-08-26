from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    input_array = list(map(int, stdin.readline().split()))
    input_array = [0] + input_array
    input_array.sort()

    visited = [False] * (N + 1)
    for idx in range(1, N + 1):
        permuation(idx, N, M, 0, visited, input_array, [])


def permuation(cur_idx, n, m, selected_idx, visited, array, answer):
    # 1. 체크인
    visited[cur_idx] = True
    selected_idx += 1
    # 2. 목적지
    answer.append(str(array[cur_idx]))
    # 3. 인접 노드 순회
    for next_idx in range(1, n + 1):
        # 4. 갈 수 있는지 검사
        if not visited[next_idx] and selected_idx != m:
            permuation(next_idx, n, m, selected_idx, visited, array, answer)
    # 5. 체크 아웃
    if len(answer) == m:
        print(' '.join(answer))
    answer.pop()
    visited[cur_idx] = False
    selected_idx -= 1


if __name__ == "__main__":
    main()
