from sys import stdin
from collections import deque

stdin = open("./input.txt", "r")
num_of_computer = int(stdin.readline())
num_of_relation = int(stdin.readline())

network = {}

for computer in range(1, num_of_computer + 1):
    network[computer] = []

for _ in range(num_of_relation):
    computer1, computer2 = map(int, stdin.readline().split())
    network[computer1].append(computer2)
    network[computer2].append(computer1)

visited = [False] * (num_of_computer + 1)

infected = 0


def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = True

    while queue:
        global infected
        cur_computer = queue.popleft()
        infected += 1

        for next_computer in network[cur_computer]:
            if not visited[next_computer]:
                visited[next_computer] = True
                queue.append(next_computer)


def main():
    bfs()
    print(infected - 1)


if __name__ == '__main__':
    main()