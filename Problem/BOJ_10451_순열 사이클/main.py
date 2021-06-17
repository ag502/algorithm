from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)


class Main:
    def __init__(self):
        self.length_of_seq = 0
        self.sequence = None
        self.graph = None
        self.visited = None
        self.finished = None
        self.num_of_cycle = None

        self.main()

    def dfs(self, cur_node):
        self.visited[cur_node] = True

        for next_node in self.graph[cur_node]:
            if not self.visited[next_node]:
                self.dfs(next_node)

            if not self.finished[next_node]:
                self.num_of_cycle += 1

        self.finished[cur_node] = True

    def main(self):
        stdin = open("./input.txt", "r")
        test_case = int(stdin.readline())

        for _ in range(test_case):
            self.graph = {}
            self.num_of_cycle = 0
            self.length_of_seq = int(stdin.readline())
            self.sequence = list(map(int, stdin.readline().split()))

            self.visited = [False] * (self.length_of_seq + 1)
            self.finished = [False] * (self.length_of_seq + 1)

            for node in range(1, self.length_of_seq + 1):
                self.graph[node] = []

            for node_1, node_2 in enumerate(self.sequence):
                self.graph[node_1 + 1].append(node_2)

            for start_node in range(1, self.length_of_seq + 1):
                if not self.visited[start_node]:
                    self.dfs(start_node)

            print(self.num_of_cycle)


if __name__ == '__main__':
    Main()