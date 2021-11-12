from sys import stdin
from collections import deque

def main():
    stdin = open('Problem\BOJ_3048_개미\input.txt')
    left_ant_num, right_ant_num = map(int, stdin.readline().split(" "))
    
    left_ants = stdin.readline().rstrip()
    right_ants = stdin.readline().rstrip()
    time = int(stdin.readline())
    
    ant_line = []
    for idx in range(left_ant_num - 1, -1, -1):
        ant_line.append([left_ants[idx], 'r'])
    for idx in range(0, right_ant_num):
        ant_line.append([right_ants[idx], 'l'])
        
    jump_ant = deque()
    for _ in range(time):
        cur_idx = 0
        while cur_idx < (left_ant_num + right_ant_num - 1):
            if ant_line[cur_idx][1] == 'r' and ant_line[cur_idx + 1][1] == 'l':
                jump_ant.append([cur_idx, cur_idx + 1])
                
                if cur_idx + 2 < left_ant_num + right_ant_num:
                    cur_idx = cur_idx + 2
                    continue
                else:
                    break
                
            cur_idx += 1
                
        while jump_ant:
            ant_1, ant_2 = jump_ant.popleft()
            ant_line[ant_1], ant_line[ant_2] = ant_line[ant_2], ant_line[ant_1]
    
    answer = ''
    for ant in ant_line:
        answer += ant[0]
        
    print(answer)
    
if __name__ == "__main__":
    main()