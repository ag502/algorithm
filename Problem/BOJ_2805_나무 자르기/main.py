from sys import stdin


# def main():
#     n, m = map(int, stdin.readline().split())
#     trees = sorted(list(map(int, stdin.readline().split())))
#     # heights = [i for i in range(max(trees) + 1)]
#
#     start = 0
#     end = max(trees)
#     candidate_height = []
#     while start <= end:
#         mid = (start + end) // 2
#         sum_of_cut = sum([tree - mid if tree -
#                           mid > 0 else 0 for tree in trees])
#
#         if sum_of_cut == m:
#             print(mid)
#             return
#         elif sum_of_cut > m:
#             start = mid + 1
#             candidate_height.append(mid)
#         elif sum_of_cut < m:
#             end = mid - 1
#
#     print(max(candidate_height))
#
#
# if __name__ == "__main__":
#     main()


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
    end = 1000000000

    while start <= end:
        mid = (start + end) // 2
        get_tree_height = get_tree(tree_height, mid)

        if get_tree_height <= target_height:
            end = mid - 1
        else:
            start = mid + 1
    print(start)


if __name__ == '__main__':
    main()