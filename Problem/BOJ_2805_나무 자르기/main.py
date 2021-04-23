from sys import stdin


def get_tree(trees, cur_height):
    height_sum = 0

    for tree in trees:
        if tree > cur_height:
            height_sum += tree - cur_height

    return height_sum


def main():
    stdin = open("./input.txt", "r")
    num_of_tree, target_height = map(int, stdin.readline().split())
    tree_height = list(map(int, stdin.readline().split()))

    start = 0
    end = max(tree_height)

    while start <= end:
        mid = (start + end) // 2
        get_tree_height = get_tree(tree_height, mid)

        if get_tree_height < target_height:
            end = mid - 1
        else:
            start = mid + 1
    print(end)


if __name__ == '__main__':
    main()