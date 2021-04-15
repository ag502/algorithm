from sys import stdin
from collections import deque

stdin = open("./input.txt", "r")
num_of_students, num_of_relations, cur_cost = map(int, stdin.readline().split())
cost = [0] + list(map(int, stdin.readline().split()))


def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    min_cost = cost[start]
    parent = start

    while queue:
        cur_student = queue.popleft()
        if min_cost > cost[cur_student]:
            min_cost = cost[cur_student]
            parent = cur_student

        for next_student in graph[cur_student]:
            if not visited[next_student]:
                queue.append(next_student)
                visited[next_student] = True

    return parent


def main():
    global cur_cost

    relation = {}
    for student in range(1, num_of_students + 1):
        relation[student] = []

    for _ in range(num_of_relations):
        student_1, student_2 = map(int, stdin.readline().split())
        relation[student_1].append(student_2)
        relation[student_2].append(student_1)

    visited = [False] * (num_of_students + 1)
    parents = deque()
    for student in range(1, num_of_students + 1):
        if not visited[student]:
            parents.append(bfs(relation, student, visited))

    answer = 0
    while parents:
        cur_parent = parents.popleft()
        if cur_cost < cost[cur_parent]:
            print("Oh no")
            return
        cur_cost -= cost[cur_parent]
        answer += cost[cur_parent]

    print(answer)


if __name__ == '__main__':
    main()