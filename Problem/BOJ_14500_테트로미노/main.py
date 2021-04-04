from sys import stdin

blocks = [
    [[0, 0], [0, 1], [0, 2], [0, 3]], # '-' 모양
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 0], [0, 1], [1, 0], [1, 1]], # 'ㅁ' 모양
    [[0, 0], [1, 0], [2, 0], [2, 1]], # 'L' 모양
    [[0, 0], [0, 1], [0, 2], [1, 0]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[1, 0], [1, 1], [1, 2], [0, 2]],
    [[2, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [1, 0], [1, 1], [2, 1]], # 'Z' 모양
    [[1, 0], [1, 1], [0, 1], [0, 2]],
    [[1, 0], [2, 0], [1, 1], [0, 1]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 1]], # 'ㅗ' 모양
    [[1, 0], [1, 1], [0, 1], [2, 1]],
    [[0, 1], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [1, 0], [2, 0], [1, 1]]
]


def apply_tetromino(cur_row, cur_col):
    sum_of_area = 0
    for i in range(19):
        temp = 0
        for j in range(4):
            next_row  = cur_row + blocks[i][j][0]
            next_col = cur_col + blocks[i][j][1]
            if (0 <= next_row < rows and 0 <= next_col < cols):
                temp += paper[next_row][next_col]
        sum_of_area = max(sum_of_area, temp)
    return sum_of_area


def main():
    stdin = open("Problem/BOJ_14500_테트로미노/input.txt", "r")
    global rows, cols, paper 
    rows, cols = map(int, stdin.readline().split())
    
    paper =[]
    for _ in range(rows):
        paper.append(list(map(int, stdin.readline().split())))
    
    answer = 0
    for row in range(rows):
        for col in range(cols):
            answer = max(apply_tetromino(row, col), answer)
    
    print(answer)
    

if __name__ == "__main__":
    main()