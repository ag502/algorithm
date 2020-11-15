from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

moving_direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def see_picture(picture, visited, n, color, cur_row, cur_col, blindness):
    # 1. 방문
    visited[cur_row][cur_col] = True
    # 2. 갈 수 있는 곳 탐색
    for moving_row, moving_col in moving_direction:
        next_row = cur_row + moving_row
        next_col = cur_col + moving_col
        # 3. 갈 수 있는 곳인지 검사
        if 0 <= next_row < n and 0 <= next_col < n:
            # 정상
            if not blindness:
                if picture[next_row][next_col] == color and not visited[next_row][next_col]:
                    see_picture(picture, visited, n, color, next_row, next_col, False)
            # 색맹
            else:
                if not visited[next_row][next_col]:
                    if color == 'R' or color == 'G':
                        if picture[next_row][next_col] in ['R', 'G']:
                            see_picture(picture, visited, n, picture[next_row][next_col], next_row, next_col, True)
                    else:
                        if picture[next_row][next_col] == color:
                            see_picture(picture, visited, n, color, next_row, next_col, True)

def main():
    stdin = open('./test_case.txt', 'r')
    n = int(stdin.readline())
    picture = []

    for _ in range(n):
        pixels = list(stdin.readline().rstrip())
        picture.append(pixels)

    # 정상
    answer = []
    for cur_color in ['R', 'G', 'B']:
        temp = 0
        visited = [[False] * n for _ in range(n)]
        for row in range(len(picture)):
            for col in range(len(picture[row])):
                if not visited[row][col] and picture[row][col] == cur_color:
                    see_picture(picture, visited, n, cur_color, row, col, False)
                    temp += 1
        answer.append(temp)

    # 색맹
    answer_2 = []
    for cur_color in ['R', 'G', 'B']:
        temp = 0
        visited = [[False] * n for _ in range(n)]
        for row in range(len(picture)):
            for col in range(len(picture[row])):
                if not visited[row][col]:
                    if cur_color == 'R' or cur_color == 'G':
                        if picture[row][col] in ['R', 'G']:
                            see_picture(picture, visited, n, cur_color, row, col, True)
                            temp += 1
                    else:
                        if picture[row][col] == cur_color:
                            see_picture(picture, visited, n, cur_color, row, col, True)
                            temp += 1
        answer_2.append(temp)

    print(str(sum(answer)) + ' ' + str(sum(answer_2[1:])))


if __name__ == '__main__':
    main()