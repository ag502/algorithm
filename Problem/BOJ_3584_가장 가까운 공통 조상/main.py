from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)


class Main:
    def __init__(self):
        self.tree = None

        self.main()

    def dfs(self, cur_node, visited, temp):
        if type(temp) is set:
            temp.add(cur_node)
        else:
            temp.append(cur_node)
        visited[cur_node] = True

        for next_node in self.tree[cur_node]:
            if not visited[next_node]:
                return self.dfs(next_node, visited, temp)
        return temp

    def main(self):
        stdin = open("./input.txt", "r")
        test_case = int(stdin.readline())

        for _ in range(test_case):
            num_of_nodes = int(stdin.readline())

            self.tree = {}
            for node in range(1, num_of_nodes + 1):
                self.tree[node] = []

            for _ in range(num_of_nodes - 1):
                parent_node, child_node = map(int, stdin.readline().split())
                self.tree[child_node].append(parent_node)

            node_1, node_2 = map(int, stdin.readline().split())

            # print(self.tree)
            # print(node_1, node_2)

            visited = [False] * (num_of_nodes + 1)
            node_1_parent = self.dfs(node_1, visited, [])

            visited = [False] * (num_of_nodes + 1)
            node_2_parent = self.dfs(node_2, visited, set())

            for node in node_1_parent:
                if node in node_2_parent:
                    print(node)
                    break


if __name__ == '__main__':
    Main()