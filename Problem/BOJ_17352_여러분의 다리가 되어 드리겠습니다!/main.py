from sys import stdin, setrecursionlimit
setrecursionlimit(10000)

def find(island, parents):
    if parents[island] == island:
        return island
    parents[island] = find(parents[island], parents)
    return parents[island]

def main():
    stdin = open('./test_case.txt', 'r')
    islands = int(stdin.readline())
    parents = [i for i in range(islands + 1)]

    for _ in range(islands - 2):
        island_1, island_2 = map(int, stdin.readline().split())
        island_1_root = find(island_1, parents)
        island_2_root = find(island_2, parents)
        parents[island_2_root] = island_1_root

    roots = set()
    for island in parents[1:]:
        roots.add(find(island, parents))

    print(' '.join(map(str, list(roots))))

if __name__ == '__main__':
    main()