from sys import stdin
from collections import deque

def main():
    gears = []
    gears.append(deque(list(stdin.readline().rstrip())))
    gears.append(deque(list(stdin.readline().rstrip())))
    gears.append(deque(list(stdin.readline().rstrip())))
    gears.append(deque(list(stdin.readline().rstrip())))

    gears_overlap = [[0, 0] for _ in range(4)]

    rotation_num = int(stdin.readline().rstrip())

    for _ in range(rotation_num):
        rotation_gear, rotation_dir = map(int, stdin.readline().split())

        for gear_num in range(4):
            gears_overlap[gear_num][0] = gears[gear_num][6]
            gears_overlap[gear_num][1] = gears[gear_num][2]

        rotation(gears[rotation_gear - 1], rotation_dir)

        cur_gear = rotation_gear
        next_rotation_dir = rotation_dir
        for gear_num in range(rotation_gear - 1, 0, -1):
            if gears_overlap[cur_gear - 1][0] != gears_overlap[gear_num - 1][1]:
                next_rotation_dir = -next_rotation_dir
                rotation(gears[gear_num - 1], next_rotation_dir)
                cur_gear = gear_num
            else:
                break

        cur_gear = rotation_gear
        next_rotation_dir = rotation_dir
        for gear_num in range(rotation_gear + 1, 5, 1):
            if gears_overlap[cur_gear - 1][1] != gears_overlap[gear_num - 1][0]:
                next_rotation_dir = -next_rotation_dir
                rotation(gears[gear_num - 1], next_rotation_dir)
                cur_gear = gear_num
            else:
                break

    answer = 0
    for idx, gear in enumerate(gears):
        if gear[0] == '1':
            if idx == 0:
                answer += 1
            elif idx == 1:
                answer += 2
            elif idx == 2:
                answer += 4
            elif idx == 3:
                answer += 8
    print(answer)

def rotation(gear, direction):
    if direction == -1:
        gear.append(gear.popleft())
    elif direction == 1:
        gear.appendleft(gear.pop())

if __name__ == '__main__':
    main()
