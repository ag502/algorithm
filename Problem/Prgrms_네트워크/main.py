def dfs(computers, cur_computer, visited):
    # 1. 방문
    visited[cur_computer] = True
    # 2. 주변 컴퓨터 탐색
    for next_computer, connected in enumerate(computers[cur_computer]):
        # 3. 탐색 가능 여부 확인
        if next_computer != cur_computer and connected == 1 and not visited[next_computer]:
            # 4. 간다
            dfs(computers, next_computer, visited)

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for start_computer in range(n):
        if not visited[start_computer]:
            answer += 1
            dfs(computers, start_computer, visited)
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))