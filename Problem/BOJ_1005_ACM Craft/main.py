from sys import stdin, maxsize
from collections import deque


def main():
    stdin = open("./input.txt", "r")
    test_case = int(stdin.readline())

    queue = deque()

    for _ in range(test_case):
        num_of_building, num_of_sequence = map(int, stdin.readline().split())
        build_times = [0] + list(map(int, stdin.readline().split()))

        sequences = {}
        for building in range(1, num_of_building + 1):
            sequences[building] = []

        in_degree = [0] * (num_of_building + 1)
        for _ in range(num_of_sequence):
            building1, building2 = map(int, stdin.readline().split())
            sequences[building1].append(building2)
            in_degree[building2] += 1

        target_building = int(stdin.readline())

        queue.clear()
        times = [0] * (num_of_building + 1)
        for building, degree in enumerate(in_degree):
            if building != 0 and degree == 0:
                queue.append(building)
                times[building] = build_times[building]

        while queue:
            cur_building = queue.popleft()
            for next_building in sequences[cur_building]:
                times[next_building] = max(times[next_building], times[cur_building] + build_times[next_building])
                in_degree[next_building] -= 1
                if in_degree[next_building] == 0:
                    queue.append(next_building)

        print(times[target_building])


if __name__ == '__main__':
    main()