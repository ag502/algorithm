from sys import stdin

def attach_paper(white_paper, coordinate):
    col, row = coordinate
    # print(col, row)
    for i in range(row, row + 10):
        for j in range(col, col + 10):
            white_paper[i][j] = 1

def main():
    white_paper = [[0] * 101 for _ in range(101)]
    num_of_paper = int(stdin.readline())
    coord_list = []
    for _ in range(num_of_paper):
        coord = tuple(map(int, stdin.readline().split()))
        coord_list.append(coord)

    for coordinate in coord_list:
        attach_paper(white_paper, coordinate)

    # print(white_paper)

    sum_of_area = 0
    for width in white_paper:
        sum_of_area += width.count(1)
    print(sum_of_area)

if __name__ == '__main__':
    main()

