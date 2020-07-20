def move(command, coord):
    x, y = coord
    if command == 'U':
        y += 1
    elif command == 'D':
        y -= 1
    elif command == 'R':
        x += 1
    else:
        x -= 1
    return x, y


def solution(dirs):
    answer = 0
    tracking = {}
    current_position = (0, 0)
    for dir in dirs:
        prev_position = current_position
        x_pos, y_pos = move(dir, prev_position)
        if x_pos > 5 or x_pos < -5 or y_pos > 5 or y_pos < -5:
            continue
        current_position = (x_pos, y_pos)
        if prev_position not in tracking:
            tracking[prev_position] = []
        if current_position not in tracking:
            tracking[current_position] = []

        for pos in tracking[prev_position]:
            if pos[0] == current_position[0] and pos[1] == current_position[1]:
                break
            else:
                tracking[prev_position].append(current_position)

        for pos in tracking[current_position]:
            if pos[0] == prev_position[0] and pos[1] == prev_position[1]:
                break
            else:
                tracking[current_position].append(prev_position)
                answer += 1

    return answer
