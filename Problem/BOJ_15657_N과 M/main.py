from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    input_array = list(map(int, stdin.readline().split()))
    input_array.sort()

    for idx in range(N):
        m_combination(idx, N, M, 0, input_array, [])


def m_combination(cur_idx, n, m, selected_num, array, answer):
    # 1. 체크인
    selected_num += 1
    # 2. 목적지
    answer.append(str(array[cur_idx]))
    # 3. 인접한 노드 순회
    for next_idx in range(cur_idx, n):
        # 4. 갈 수 있는지 검사
        if selected_num != m:
            m_combination(next_idx, n, m, selected_num, array, answer)
    # 5. 체크아웃
    if len(answer) == m:
        print(' '.join(answer))
    answer.pop()
    selected_num -= 1


if __name__ == "__main__":
    main()
