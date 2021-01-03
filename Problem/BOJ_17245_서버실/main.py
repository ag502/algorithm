from sys import stdin


def can_operate(server_room, time):
    num_of_operate_computer = 0
    for i in range(len(server_room)):
        for j in range(len(server_room[i])):
            if server_room[i][j] < time:
                num_of_operate_computer += server_room[i][j]
            else:
                num_of_operate_computer += time
    return num_of_operate_computer


def binary_search(server_room, total_computer):
    start_time = 0
    end_time = 10 ** 7

    while start_time <= end_time:
        mid_time = (start_time + end_time) // 2
        num_operate_computer = can_operate(server_room, mid_time)
        if (num_operate_computer * 100 / total_computer) >= 50:
            end_time = mid_time - 1
        else:
            start_time = mid_time + 1
    return start_time



def main():
    stdin = open('./input.txt', 'r')
    n = int(stdin.readline())

    total_server_computer = 0
    server_room = []
    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        server_room.append(row)
        total_server_computer += sum(row)

    if total_server_computer == 0:
        print(0)
        return

    time = binary_search(server_room, total_server_computer)
    print(time)


if __name__ == '__main__':
    main()