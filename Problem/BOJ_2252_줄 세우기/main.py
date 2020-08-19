from sys import stdin
from collections import deque


def main():
    N, M = map(int, stdin.readline().split())

    # in_degree 배열 선언
    in_degree = [0] * (N + 1)

    # 학생 키 인접 리스트, in_degree 초기화
    student_adj = {}
    for i in range(1, N + 1):
        student_adj[i] = []

    for _ in range(M):
        A, B = map(int, stdin.readline().split())
        student_adj[A].append(B)
        in_degree[B] += 1

    # 위상 정렬
    queue = deque()
    answer = []

    # in_degree가 0인 학생 queue에 추가
    for student, degree in enumerate(in_degree):
        if student != 0 and degree == 0:
            queue.append(student)

    # 학생 수 만큼 반복
    for _ in range(N):
        if not queue:
            return

        cur_student = queue.popleft()
        answer.append(str(cur_student))

        for next_student in student_adj[cur_student]:
            in_degree[next_student] -= 1
            if in_degree[next_student] == 0:
                queue.append(next_student)

    print(' '.join(answer))


if __name__ == "__main__":
    main()
