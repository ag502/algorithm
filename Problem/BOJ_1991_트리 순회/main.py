from sys import stdin

tree = [None] * 26

class Node:
    def __init__(self, cur_node, left_node, right_node):
        self.cur_node = cur_node
        self.left_node = left_node
        self.right_node = right_node

def in_order(root, answer):
    if root.left_node is not None:
        in_order(tree[ord(root.left_node) - ord('A')], answer)
    answer.append(root.cur_node)
    if root.right_node is not None:
        in_order(tree[ord(root.right_node) - ord('A')], answer)

def post_order(root, answer):
    if root.left_node is not None:
        post_order(tree[ord(root.left_node) - ord('A')], answer)
    if root.right_node is not None:
        post_order(tree[ord(root.right_node) - ord('A')], answer)
    answer.append(root.cur_node)

def pre_order(root, answer):
    answer.append(root.cur_node)
    if root.left_node is not None:
        pre_order(tree[ord(root.left_node) - ord('A')], answer)
    if root.right_node is not None:
        pre_order(tree[ord(root.right_node) - ord('A')], answer)

def main():
    stdin = open('./input.txt', 'r')
    num_of_node = int(stdin.readline())

    for _ in range(num_of_node):
        cur_node, left_node, right_node = stdin.readline().rstrip().split()

        if left_node == '.':
            left_node = None
        if right_node == '.':
            right_node = None

        tree[ord(cur_node) - ord('A')] = Node(cur_node, left_node, right_node)
    # print(tree[0].right_node)
    answer = []
    pre_order(tree[0], answer)
    print(''.join(answer))

    answer = []
    in_order(tree[0], answer)
    print(''.join(answer))

    answer = []
    post_order(tree[0], answer)
    print(''.join(answer))

if __name__ == '__main__':
    main()