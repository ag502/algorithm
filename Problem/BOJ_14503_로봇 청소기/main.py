from sys import stdin

moving_coord = [[-1, 0], [0, 1], [1, 0], [0, -1]]
directions = [0, 1, 2, 3]

def main():
    # stdin = open('./test_case.txt', 'r')
    rows, cols = map(int, stdin.readline().split())
    cur_pos_row, cur_pos_col, cur_dir = map(int, stdin.readline().split())
    cleaning_area = []

    for _ in range(rows):
        row = list(map(int, stdin.readline().split()))
        cleaning_area.append(row)

    cleaning(cleaning_area, cur_pos_row, cur_pos_col, cur_dir, rows, cols)
    # print(cleaning_area)

    answer = 0
    for row in range(rows):
        for col in range(cols):
            if cleaning_area[row][col] == -1:
                answer += 1
    print(answer)

    # print(cleaning_area)

def cleaning(graph, cur_row, cur_col, cur_dir, rows, cols):
    # 청소
    graph[cur_row][cur_col] = -1
    # print(cur_row, cur_col)
    is_cleaned = False

    # 갈 수 있는곳 탐색
    for i in range(1, 5):
        next_dir = directions[cur_dir - i]
        next_row = cur_row + moving_coord[next_dir][0]
        next_col = cur_col + moving_coord[next_dir][1]

        # 조건에 부합하면 전진
        if 0 <= next_row < rows and 0 <= next_col < cols:
            if graph[next_row][next_col] == 0:
                is_cleaned = True
                cleaning(graph, next_row, next_col, next_dir, rows, cols)
                break

    if not is_cleaned:
        next_row = cur_row - moving_coord[cur_dir][0]
        next_col = cur_col - moving_coord[cur_dir][1]
        if 0 <= next_row < rows and 0 <= next_col < cols:
            if graph[next_row][next_col] != 1:
                cleaning(graph, next_row, next_col, cur_dir, rows, cols)

if __name__ == '__main__':
    main()