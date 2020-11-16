from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

def find(island, parents):
    if parents[island] == island:
        return island
    parents[island] = find(parents[island], parents)
    return parents[island]

def merge(island_1, island_2, parents, ranks):
    island_1_root = find(island_1, parents)
    island_2_root = find(island_2, parents)
    if island_1_root == island_2_root:
        return

    if ranks[island_2_root] > ranks[island_1_root]:
        temp = ranks[island_1_root]
        ranks[island_1_root] = ranks[island_2_root]
        ranks[island_2_root] = temp

    parents[island_2_root] = island_1_root

    if ranks[island_1_root] == ranks[island_2_root]:
        ranks[island_1_root] += 1

def main():
    stdin = open('./test_case.txt', 'r')
    islands = int(stdin.readline())
    parents = [i for i in range(islands + 1)]
    ranks = [0] * (islands + 1)

    for _ in range(islands - 2):
        island_1, island_2 = map(int, stdin.readline().split())
        merge(island_1, island_2, parents, ranks)

    roots = set()
    for island in parents[1:]:
        roots.add(find(island, parents))

    print(' '.join(map(str, list(roots))))

if __name__ == '__main__':
    main()