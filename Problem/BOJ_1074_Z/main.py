from sys import stdin
import operator

def partition(start, end, n):
    position_list = []
    next_square_length = 2 ** (n - 1)

    for i in range(4):
        if i == 0:
            new_start_position = start
        elif i == 1:
            new_start_position = tuple(map(operator.add, start, (0, next_square_length)))
        elif i == 2:
            new_start_position = tuple(map(operator.add, start, (next_square_length, 0)))
        else:
            new_start_position = tuple(map(operator.add, start, (next_square_length, next_square_length)))
        new_end_position = tuple(map(operator.add, new_start_position, (next_square_length - 1, next_square_length - 1)))
        position_list.append([new_start_position, new_end_position])

    return position_list

def main():
    n, r, c = map(int, stdin.readline().split())
    start = (0, 0)
    end = (2 ** n - 1, 2 ** n - 1)
    i_th = 0
    for i in range(n , 0, -1):
        position_list = partition(start, end, i)
        for index, position in enumerate(position_list):
            sub_start, sub_end = position
            if sub_start[0] <= r <= sub_end[0] and sub_start[1] <= c <= sub_end[1]:
                start = sub_start
                end = sub_end
                i_th += index * ((2 ** (i - 1)) ** 2)

    print(i_th)

if __name__ == '__main__':
    main()