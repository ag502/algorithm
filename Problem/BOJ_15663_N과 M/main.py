from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    input_array = [0] + list(map(int, stdin.readline().split()))
    input_array.sort()

    visited = [False] * (N + 1)
    # for idx in range(N):
    permutation(0, N, M, -1, input_array, visited, [])


def permutation(cur_idx, n, m, selected_num, array, visited, answer):
    # 1. 체크인
    visited[cur_idx] = True
    selected_num += 1
    # 2. 도착
    if cur_idx != 0:
        answer.append(str(array[cur_idx]))
    # 3. 인접노드 순회
    temp = -1
    for next_idx in range(1, n + 1):
        # 4. 갈 수 있는지 검사
        if selected_num != m and not visited[next_idx] and temp != array[next_idx]:
            temp = array[next_idx]
            permutation(next_idx, n, m, selected_num,
                        array, visited, answer)
    # 5. 체크아웃
    if len(answer) == m:
        answer_str = ' '.join(answer)
        print(answer_str)
    if cur_idx != 0:
        answer.pop()
    visited[cur_idx] = False
    selected_num -= 1


if __name__ == "__main__":
    main()
