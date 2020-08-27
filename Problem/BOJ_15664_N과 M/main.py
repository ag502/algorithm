from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    input_array = [0] + list(map(int, stdin.readline().split()))
    input_array.sort()

    visited = [False] * (N + 1)
    combination(0, N, M, -1, visited, input_array, [])


def combination(cur_idx, n, m, selected_idx, visited, array, answer):
    # 1. 체크인
    visited[cur_idx] = True
    selected_idx += 1
    # 2. 목적지
    if cur_idx != 0:
        answer.append(str(array[cur_idx]))
    # 3. 인접 노드 순회
    temp = -1
    for next_idx in range(cur_idx + 1, n + 1):
        # 4. 갈 수 있는 지 검사
        if selected_idx != m and not visited[next_idx] and temp != array[next_idx]:
            # print(temp, array[next_idx])
            temp = array[next_idx]
            combination(next_idx, n, m, selected_idx,
                        visited, array, answer)
    # 5. 체크아웃
    if len(answer) == m:
        answer_str = ' '.join(answer)
        print(answer_str)
    if cur_idx != 0:
        answer.pop()
    visited[cur_idx] = False
    selected_idx -= 1


if __name__ == "__main__":
    main()
