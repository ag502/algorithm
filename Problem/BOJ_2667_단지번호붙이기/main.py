from sys import stdin

moving_row = [-1, 0, 1, 0]
moving_col = [0, 1, 0, -1]

def main():
    # file = open('./test_case.txt', 'r')

    n = int(stdin.readline())
    apt_map = []
    for _ in range(n):
        row = list(map(int, list(stdin.readline().rstrip())))
        apt_map.append(row)

    count = 0
    answer = []
    for row in range(n):
        for col in range(n):
            if apt_map[row][col] == 1:
                count += 1
                answer.append(dfs(apt_map, row, col, n))
    answer.sort()

    print(count)
    for num in answer:
        print(num)


def dfs(graph, cur_pos_row, cur_pos_col, n):
    # 1.방문
    graph[cur_pos_row][cur_pos_col] = -1
    answer = 1
    # 2.갈 수 있는 곳 탐색
    for moving_row_dir, moving_col_dir in zip(moving_row, moving_col):
        next_pos_row = cur_pos_row + moving_row_dir
        next_pos_col = cur_pos_col + moving_col_dir
        if 0 <= next_pos_row < n and 0 <= next_pos_col < n:
            if graph[next_pos_row][next_pos_col] == 1:
                # 3.간다
                answer += dfs(graph, next_pos_row, next_pos_col, n)
    return answer
if __name__ == '__main__':
    main()