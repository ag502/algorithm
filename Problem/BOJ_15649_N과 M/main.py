from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())

    for i in range(1, N + 1):
        visited = [0] * (N + 1)
        permutation(i, 0, N, M, [], visited)


def permutation(cur_num, selected_num, n, m, answer, visited):
    # 1. 방문
    selected_num += 1
    visited[cur_num] = -1
    # 2. 도착
    answer.append(cur_num)
    # 3. 인접 노드 순회
    for i in range(1, n + 1):
        # 4. 갈 수 있는지 검사
        if selected_num < m and visited[i] != -1 and i != cur_num:
            # 5. 간다
            permutation(i, selected_num, n, m, answer, visited)
    # 5. 체크아웃
    if len(answer) == m:
        print(" ".join(map(str, answer)))
    answer.pop()
    selected_num -= 1
    visited[cur_num] = 0


if __name__ == "__main__":
    main()
