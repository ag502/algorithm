from sys import stdin
from collections import deque
from heapq import heappush, heappop, heapify


def main():
    N, M = map(int, stdin.readline().split())
    problem_adj = {}
    for i in range(1, N + 1):
        problem_adj[i] = []

    in_degree = [0] * (N + 1)

    for _ in range(M):
        p1, p2 = map(int, stdin.readline().split())
        problem_adj[p1].append(p2)
        in_degree[p2] += 1

    pq = []
    answer = []
    for idx in range(1, len(in_degree)):
        problem_num = idx
        degree = in_degree[idx]
        if degree == 0:
            heappush(pq, problem_num)

    for _ in range(N):
        if not pq:
            return

        # cur_problem = queue.popleft()
        cur_problem = heappop(pq)
        answer.append(cur_problem)

        for problem_num in problem_adj[cur_problem]:
            in_degree[problem_num] -= 1
            if in_degree[problem_num] == 0:
                # queue.append(problem_num)
                heappush(pq, problem_num)

    print(' '.join(map(str, answer)))


if __name__ == "__main__":
    main()
