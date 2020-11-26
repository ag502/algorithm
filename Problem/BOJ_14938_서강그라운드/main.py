from sys import stdin

def dfs(field, items, visited, search_range, cur_point, acc_items, acc_distance):
    # 1. 방문
    visited[cur_point] = True
    acc_items[cur_point] = items[cur_point]

    # 2. 갈 수 있는 곳 탐색
    for next_point, next_distance in field[cur_point]:
        # 3. 갈 수 있는지 확인
        if not visited[next_point] and acc_distance + next_distance <= search_range:
            dfs(field, items, visited, search_range, next_point, acc_items, acc_distance + next_distance)
    # 4. 체크 아웃
    visited[cur_point] = False


def main():
    stdin = open('./input.txt', 'r')
    num_of_points, search_range, num_of_paths = map(int, stdin.readline().split())
    items = [0] + list(map(int, stdin.readline().split()))
    field = {}

    for i in range(1, num_of_points + 1):
        field[i] = []

    for _ in range(num_of_paths):
        point_1, point_2, distance = map(int, stdin.readline().split())
        field[point_1].append([point_2, distance])
        field[point_2].append([point_1, distance])

    answer = 0
    for point in range(1, num_of_points + 1):
        visited = [False] * (num_of_points + 1)
        temp_answer = {}
        dfs(field, items, visited, search_range, point, temp_answer, 0)

        sum_of_item = 0
        for _, item in temp_answer.items():
            sum_of_item += item

        answer = max(answer, sum_of_item)
    print(answer)

if __name__ == '__main__':
    main()