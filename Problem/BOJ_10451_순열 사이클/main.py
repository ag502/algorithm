from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)


class Main:
    def __init__(self):
        self.length_of_seq = 0
        self.sequence = None
        self.parent = None

        self.main()

    def find(self, cur_node):
        if self.parent[cur_node] == cur_node:
            return cur_node
        self.parent[cur_node] = self.find(self.parent[cur_node])
        return self.parent[cur_node]

    def merge(self, node_1, node_2):
        node_1_parent = self.find(node_1)
        node_2_parent = self.find(node_2)

        if node_1_parent == node_2_parent:
            return True
        self.parent[node_2_parent] = node_1_parent
        return False

    def main(self):
        stdin = open("./input.txt", "r")
        test_case = int(stdin.readline())

        for _ in range(test_case):
            self.length_of_seq = int(stdin.readline())
            self.sequence = list(map(int, stdin.readline().split()))
            self.parent = [i for i in range(self.length_of_seq + 1)]

            num_of_cycle = 0
            for node_1, node_2 in enumerate(self.sequence):
                is_cycle = self.merge(node_1 + 1, node_2)
                if is_cycle:
                    num_of_cycle += 1

            print(num_of_cycle)


if __name__ == '__main__':
    Main()