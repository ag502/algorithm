from sys import stdin
from collections import deque

def rotation_gear(gear, direction):
    if direction == -1:
        gear.append(gear.popleft())
    elif direction == 1:
        gear.appendleft(gear.pop())

def main():
    gears = {}
    for i in range(1, 5):
        gears[i] = deque(list(stdin.readline().rstrip()))

    rotation_num = int(stdin.readline())
    for _ in range(rotation_num):
        meeting_point = [0, (-1, gears[1][2]), (gears[2][6], gears[2][2]), (gears[3][6], gears[3][2]), (gears[4][6], -1)]
        selected_gear, direction = map(int, stdin.readline().split())

        rotation_gear(gears[selected_gear], direction)
        start_point = meeting_point[selected_gear][1]
        for i in range(selected_gear + 1, len(meeting_point)):
            if start_point != meeting_point[i][0]:
                direction = -direction
                rotation_gear(gears[i], direction)
            else:
                break
            start_point = meeting_point[i][1]

        start_point = meeting_point[selected_gear][0]
        for i in range(selected_gear - 1, 0, -1):
            if start_point != meeting_point[i][1]:
                direction = -direction
                rotation_gear(gears[i], direction)
            else:
                break
            start_point = meeting_point[i][0]

    score = 0
    for gear_num in gears:
        # print(gear_num)
        if gear_num == 1:
            score += int(gears[gear_num][0]) * 1
        elif gear_num == 2:
            score += int(gears[gear_num][0]) * 2
        elif gear_num == 3:
            score += int(gears[gear_num][0]) * 4
        else:
            score += int(gears[gear_num][0]) * 8
    print(score)

if __name__ == '__main__':
    main()
