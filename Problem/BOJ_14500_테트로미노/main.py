from sys import stdin


def apply_tetromino():
    sum_of_block = 0
    # 가로 4칸
    for row in range(rows):
        for col in range(cols - 3):
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row][col + 1] + paper[row][col + 2] + paper[row][col + 3])
    # 세로 4칸
    for row in range(rows - 3):
        for col in range(cols):
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row + 1][col] + paper[row + 2][col] + paper[row + 3][col])
    
    # 정사각형
    for row in range(rows - 1):
        for col in range(cols - 1):
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row][col + 1] + paper[row + 1][col] + paper[row + 1][col + 1])
    
    # 'L'자 (1), (5)
    for row in range(rows - 2):
        for col in range(cols - 1):
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row + 1][col] + paper[row + 2][col] + paper[row + 2][col + 1])
            sum_of_block = max(sum_of_block, paper[row + 2][col] + paper[row][col + 1] + paper[row + 1][col + 1] + paper[row + 2][col + 1])

    # 'L'자 (2), (6)
    for row in range(rows - 1):
        for col in range(cols - 2):
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row + 1][col] + paper[row][col + 1] + paper[row][col + 2])
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row + 1][col] + paper[row + 1][col + 1] + paper[row + 1][col + 2])
    # 'L'자 (3), (7)
    for row in range(rows - 2):
        for col in range(cols - 1):
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row][col + 1] + paper[row + 1][col + 1] + paper[row + 2][col + 1])
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row][col + 1] + paper[row + 1][col] + paper[row + 2][col])
    # 'L'자 (4), (8)
    for row in range(rows - 1):
        for col in range(cols - 2):
            sum_of_block = max(sum_of_block, paper[row + 1][col] + paper[row + 1][col + 1] + paper[row + 1][col + 2] + paper[row][col + 2])
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row][col + 1] + paper[row][col + 2] + paper[row + 1][col + 2])

    # 'ㄴㄱ'자 (1), (3)
    for row in range(rows - 2):
        for col in range(cols - 1):
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row + 1][col] + paper[row + 1][col + 1] + paper[row + 2][col + 1])
            sum_of_block = max(sum_of_block, paper[row][col + 1] + paper[row + 1][col + 1] + paper[row + 1][col] + paper[row + 2][col])
    
    # 'ㄴㄱ'자 (2), (4)
    for row in range(rows - 1):
        for col in range(cols - 2):
            sum_of_block = max(sum_of_block, paper[row + 1][col] + paper[row + 1][col + 1] + paper[row][col + 1] + paper[row][col + 2])
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row][col + 1] + paper[row + 1][col + 1] + paper[row + 1][col + 2])
            
    # 'ㅜ'자 (1), (3)
    for row in range(rows - 1):
        for col in range(cols - 2):
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row][col + 1] + paper[row][col + 2] + paper[row + 1][col + 1])
            sum_of_block = max(sum_of_block, paper[row][col + 1] + paper[row + 1][col] + paper[row + 1][col + 1] + paper[row + 1][col + 2])

    # 'ㅜ'자 (2), (4)
    for row in range(rows - 2):
        for col in range(cols - 1):
            sum_of_block = max(sum_of_block, paper[row + 1][col] + paper[row][col + 1] + paper[row + 1][col + 1] + paper[row + 2][col + 1])
            sum_of_block = max(sum_of_block, paper[row][col] + paper[row + 1][col] + paper[row + 2][col] + paper[row + 1][col + 1])
            
    print(sum_of_block)    


def main():
    stdin = open("Problem/BOJ_14500_테트로미노/input.txt", "r")
    global rows, cols, paper
    
    rows, cols = map(int, stdin.readline().split())
    paper = []
    for _ in range(rows):
        paper.append(list(map(int, stdin.readline().split())))
    
    apply_tetromino()
    

if __name__ == "__main__":
    main()