from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

cyclic_students = []


def tracking_cycle(parent_nodes, cur_student, next_student):
    cyclic_students.append(cur_student)
    if cur_student == next_student:
        return
    tracking_cycle(parent_nodes, parent_nodes[cur_student], next_student)


def dfs(cur_student, graph, visited, finished, parent_nodes):
    visited[cur_student] = True
    for next_student in graph[cur_student]:
        if not visited[next_student]:
            parent_nodes[next_student] = cur_student
            dfs(next_student, graph, visited, finished, parent_nodes)
        elif not finished[next_student]:
            tracking_cycle(parent_nodes, cur_student, next_student)

    finished[cur_student] = True


def main():
    stdin = open("./input.txt", "r")
    test_case = int(stdin.readline())

    for _ in range(test_case):
        num_of_student = int(stdin.readline())
        student_list = list(map(int, stdin.readline().split()))

        graph = {}
        visited = [False] * (num_of_student + 1)
        finished = [False] * (num_of_student + 1)
        parent_nodes = [0] * (num_of_student + 1)
        global cyclic_students
        cyclic_students = []

        for idx, student in enumerate(student_list):
            graph[idx + 1] = []
            graph[idx + 1].append(student)

        for student in range(1, num_of_student + 1):
            if not visited[student]:
                dfs(student, graph, visited, finished, parent_nodes)

        print(num_of_student - len(cyclic_students))


if __name__ == '__main__':
    main()