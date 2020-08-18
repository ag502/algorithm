from sys import stdin
from collections import deque


def main():
    N, M = map(int, stdin.readline().split())
    problem_adj = {}
    for i in range(1, N + 1):
        problem_adj[i] = []
    in_degree = [0] * (N + 1)

    queue = deque()
    solve_sequence = []

    for _ in range(M):
        start_p, end_p = map(int, stdin.readline().split())
        problem_adj[start_p].append(end_p)
        in_degree[end_p] += 1

    for problem in problem_adj.keys():
        problem_adj[problem].sort()

    for idx, degree in enumerate(in_degree[1:]):
        if degree == 0:
            queue.append((idx + 1, idx + 1))
            in_degree[idx + 1] = -1

    while queue:
        # if len(queue) != 1:
        #     for idx, degree in enumerate(in_degree[1:]):
        #         if degree == 0:
        #             queue.append(idx + 1)
        #             in_degree[idx + 1] = -1
        #             break

        here = queue.popleft()
        solve_sequence.append(here)

        for there in problem_adj[here[1]]:
            in_degree[there] -= 1
            if in_degree[there] == 0:
                queue.append((here[1], there))
                in_degree[there] = -1

    print(solve_sequence)
    solve_sequence.sort(key=lambda x: (x[0]))
    print(solve_sequence)

    string = []
    for _, problem in solve_sequence:
        string.append(str(problem))

    print(' '.join(string))


if __name__ == "__main__":
    main()
