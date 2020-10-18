from sys import stdin
from collections import deque

def main():
    stdin = open('./test_case.txt', 'r')
    test_case = int(stdin.readline())

    for _ in range(test_case):
        queue = deque()
        positions = []

        num_of_stores = int(stdin.readline())
        home_pos = list(map(int, stdin.readline().split()))
        queue.append(home_pos)

        for _ in range(num_of_stores):
            store_pos = list(map(int, stdin.readline().split()))
            positions.append(store_pos)

        destination = list(map(int, stdin.readline().split()))
        positions.append(destination)

        while len(queue) != 0:
            x_pos, y_pos = queue.popleft()

            if x_pos == destination[0] and y_pos == destination[1]:
                print("happy")
                break

            # 갈 수 있는 주변 탐색
            for idx, next_pos in enumerate(positions):
                if next_pos != -1:
                    next_x_pos, next_y_pos = next_pos
                    distance = abs(next_x_pos - x_pos) + abs(next_y_pos - y_pos)
                    if abs(distance) <= 1000:
                        queue.append([next_x_pos, next_y_pos])
                        positions[idx] = -1
        else:
            print('sad')

if __name__ == '__main__':
    main()