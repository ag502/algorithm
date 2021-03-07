from sys import stdin, maxsize
from copy import deepcopy
from itertools import permutations
from collections import deque

direction = [
    [0, 1], [1, 0], [0, -1], [-1, 0]
]


def get_array_value(array):
    answer = maxsize
    for row in array[1:]:
        answer = min(answer, sum(row))
        
    return answer


def rotation_array(commands_perm):
    array_temp = deepcopy(array)
    # print(commands_perm)
    for command in commands_perm:
        init_row, init_col, gap = command
        start_row, start_col = [init_row - gap, init_col - gap]
        end_row, end_col = [init_row + gap, init_col + gap]
        
        width = end_row - start_row + 1
        for _ in range(width // 2):
            cur_row = start_row
            cur_col = start_col
            cur_dir = 0
            queue = deque()
            while True:
                # print(cur_row, cur_col, start_row, start_col, cur_dir)
                if cur_dir != 0 and cur_row == start_row and cur_col == start_col:
                    break
                queue.append(array_temp[cur_row][cur_col])
                
                if cur_dir == 0 and cur_col >= end_col:
                    cur_dir += 1
                elif cur_dir == 1 and cur_row >= end_row:
                    cur_dir += 1
                elif cur_dir == 2 and cur_col <= start_col:
                    cur_dir += 1
                
                cur_row += direction[cur_dir][0]
                cur_col += direction[cur_dir][1]

            queue.appendleft(queue.pop())
            cur_row = start_row
            cur_col = start_col
            cur_dir = 0
            while queue:
                array_temp[cur_row][cur_col] = queue.popleft()
                
                if cur_dir == 0 and cur_col >= end_col:
                    cur_dir += 1
                elif cur_dir == 1 and cur_row >= end_row:
                    cur_dir += 1
                elif cur_dir == 2 and cur_col <= start_col:
                    cur_dir += 1
                
                cur_row += direction[cur_dir][0]
                cur_col += direction[cur_dir][1]
                
            start_row += 1
            start_col += 1
            end_row -= 1
            end_col -= 1
    
    return get_array_value(array_temp)
            

def main():
    stdin = open("Problem/BOJ_17406_배열 돌리기4/input.txt", "r")
    global rows, cols, num_of_commands, array, commands
    
    rows, cols, num_of_commands = map(int, stdin.readline().split())
    
    array = [[0] * (cols + 1)]
    commands = []
    for _ in range(rows):
        array.append([0] + list(map(int, stdin.readline().split())))
    
    for _ in range(num_of_commands):
        commands.append(list(map(int, stdin.readline().split())))
        
    commands_perms = list(permutations(commands, num_of_commands))
    
    answer = maxsize
    for commands_perm in commands_perms:
        answer = min(answer, rotation_array(commands_perm))
        
    print(answer)


if __name__ == "__main__":
    main()