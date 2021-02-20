from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    global num_of_leak_points, length_of_tape, leak_positions
    num_of_leak_points, length_of_tape = map(int, stdin.readline().split())

    leak_positions = list(map(int, stdin.readline().split()))
    leak_positions.sort()

    leak_pos_range = []
    for position in leak_positions:
        leak_pos_range.append((position - 0.5, position + 0.5))

    answer = 0
    cur_start_point, cur_end_point = leak_pos_range[0]
    for idx in range(1, len(leak_pos_range)):
        start_point, end_point = leak_pos_range[idx]
        if end_point - cur_start_point > length_of_tape:
            answer += 1
            cur_start_point = start_point
            cur_end_point = end_point

    if leak_pos_range[len(leak_pos_range) - 1][1] - cur_start_point <= length_of_tape:
        answer += 1

    print(answer)


if __name__ == '__main__':
    main()