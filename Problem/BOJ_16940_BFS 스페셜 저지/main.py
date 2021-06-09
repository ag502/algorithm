from sys import stdin
from collections import deque


class Main:
    def __init__(self):
        stdin = open("./input.txt", "r")
        self.num_of_vertex = int(stdin.readline())

        self.graph = {}
        for i in range(1, self.num_of_vertex + 1):
            self.graph[i] = set()

        for _ in range(self.num_of_vertex - 1):
            start_vertex, end_vertex = map(int, stdin.readline().split())
            self.graph[start_vertex].add(end_vertex)
            self.graph[end_vertex].add(start_vertex)
        self.visited = [False] * (self.num_of_vertex + 1)

        self.result = list(map(int, stdin.readline().split()))

        self.main()

    def bfs(self):
        ptr = 0
        queue = deque()

        queue.append(1)
        self.visited[1] = True

        if self.result[ptr] != 1:
            return False

        ptr += 1
        while queue:
            size = len(queue)
            for _ in range(size):
                temp = set()
                cur_vertex = queue.popleft()
                for next_vertex in self.graph[cur_vertex]:
                    if not self.visited[next_vertex]:
                        temp.add(next_vertex)

                for _ in range(len(temp)):
                    if self.result[ptr] in temp:
                        queue.append(self.result[ptr])
                        self.visited[self.result[ptr]] = True
                        ptr += 1
                    else:
                        return False
        return True

    def main(self):
        if self.bfs():
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    Main()