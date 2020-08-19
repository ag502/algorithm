from sys import stdin
from collections import deque


def main():
    N, M = map(int, stdin.readline().split())

    # 간선 정보 배열 초기화
    in_degree = [0] * (N + 1)

    # 가수 순서 인접 리스트 초기화
    singer_adj = {}

    for i in range(1, N + 1):
        singer_adj[i] = []

    for _ in range(M):
        singer_sequence = list(map(int, stdin.readline().split()))[1:]

        for idx, singer in enumerate(singer_sequence):
            if idx != len(singer_sequence) - 1:
                singer_adj[singer].append(singer_sequence[idx + 1])
                # in_degree 간선 하나 추가
                in_degree[singer_sequence[idx + 1]] += 1

    # 위상 정렬
    queue = deque()
    answer = []

    # in_degree가 0인 가수 모두 queue에 삽입
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)

    # 가수 수 만큼 순회
    for _ in range(N):
        if not queue:
            print(0)
            return

        cur_singer = queue.popleft()
        answer.append(cur_singer)

        for next_singer in singer_adj[cur_singer]:
            in_degree[next_singer] -= 1
            if in_degree[next_singer] == 0:
                queue.append(next_singer)

    for singer in answer:
        print(singer)


if __name__ == "__main__":
    main()
