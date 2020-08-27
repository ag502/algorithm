from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    input_array = [0] + list(map(int, stdin.readline().split()))
    input_array.sort()

    m_permutation(0, N, M, -1, input_array, [])


def m_permutation(cur_idx, n, m, selected_idx, array, answer):
    # 1. 방문
    selected_idx += 1
    # 2. 도착
    if cur_idx != 0:
        answer.append(str(array[cur_idx]))
    # 3. 인접 노드 순회
    temp = -1
    for next_idx in range(1, n + 1):
        # 4. 갈 수 있는지 검사
        if selected_idx != m and temp != array[next_idx]:
            temp = array[next_idx]
            m_permutation(next_idx, n, m, selected_idx, array, answer)
    # 5. 체크아웃
    if len(answer) == m:
        print(' '.join(answer))
    if cur_idx != 0:
        answer.pop()
    selected_idx -= 1


if __name__ == "__main__":
    main()
