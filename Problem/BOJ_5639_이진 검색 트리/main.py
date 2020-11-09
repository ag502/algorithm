from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

def post_order(node_list):
    if len(node_list) == 0:
        return []

    root = node_list[0]
    if len(node_list) == 1:
        return [root]
    left = []
    right = []
    for i in range(1, len(node_list)):
        if root > node_list[i]:
            left.append(node_list[i])
        else:
            right.append(node_list[i])
    return post_order(left) + post_order(right) + [root]


def main():
    node_list = []
    while True:
        try:
            node_list.append(int(stdin.readline()))
        except:
            break

    number_list = post_order(node_list)
    for num in number_list:
        print(num)

if __name__ == '__main__':
    main()
