from sys import stdin

class Node:
    def __init__(self, parent, left, right):
        self.__parent = parent
        self.__left = left
        self.__right = right

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, node):
        self.__parent = node

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node):
        self.__left = node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node):
        self.__right = node

def check_children(node):
    if node.left is None:
        return 'RIGHT'
    else:
        return 'LEFT'

def main():
    stdin = open('./input.txt', 'r')
    num_of_node = int(stdin.readline())

    nodes = [None] * (num_of_node + 1)
    # nodes[1] = 1
    nodes[1] = Node(None, None, None)

    for _ in range(num_of_node - 1):
        node_1, node_2 = map(int, stdin.readline().split())

        if nodes[node_1] is not None:
            # if check_children(nodes[node_1]) == 'RIGHT':
            #     nodes[node_1].right = node_2
            # else:
            #     nodes[node_1].left = node_2
            nodes[node_2] = Node(node_1, None, None)
        else:
            # if check_children(nodes[node_2]) == 'RIGHT':
            #     nodes[node_2].right = node_1
            # else:
            #     nodes[node_2].left = node_1
            nodes[node_1] = Node(node_2, None, None)

    for node in nodes[2:]:
        print(node.parent)

if __name__ == '__main__':
    main()



