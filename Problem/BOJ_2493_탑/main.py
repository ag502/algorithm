from sys import stdin
from collections import deque


def main():
    stdin = open("Problem/BOJ_2493_탑/input.txt")
    num_of_towers = int(stdin.readline())
    tower_heights = list(map(int, stdin.readline().split()))
    answer = [0] * num_of_towers
    
    tower_number = {}
    for idx, height in enumerate(tower_heights):
        tower_number[height] = idx + 1
    
    stack = deque()
    stack.append(tower_heights[0])
    for idx, height in enumerate(tower_heights[1:]):
        while True:
            top = stack[len(stack) - 1]
            if top >= height:
                answer[idx + 1] = tower_number[top]
                stack.append(height)
                break
            else:
                stack.pop()
                if not stack:
                    stack.append(height)
                    break
    
    print(' '.join(map(str,answer)))
    
if __name__ == "__main__":
    main()