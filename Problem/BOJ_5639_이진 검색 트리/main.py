from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

class BST:
    class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.parent = None
            self.data = data

    def __init__(self):
        self.root = None
        self.size = 0

    def search(self, start):
        pass

    def add(self, data):
        new_node = self.Node(data)
        if self.size == 0:
            self.root = new_node
        else:
            current_node = self.root
            prev_node = None
            is_left = False
            while current_node is not None:
                prev_node = current_node
                if current_node.data < data:
                    current_node = current_node.right
                    is_left = False
                elif current_node.data > data:
                    current_node = current_node.left
                    is_left = True

            if is_left:
                prev_node.left = new_node
            else:
                prev_node.right = new_node
            new_node.parent = prev_node
        self.size += 1

    def post_order(self, start_point):
        if start_point is None:
            return
        self.post_order(start_point.left)
        self.post_order(start_point.right)
        print(start_point.data)

def main():
    binary_search_tree = BST()
    while True:
        try:
            data = int(stdin.readline())
            binary_search_tree.add(data)
        except:
            break

    binary_search_tree.post_order(binary_search_tree.root)


if __name__ == '__main__':
    main()