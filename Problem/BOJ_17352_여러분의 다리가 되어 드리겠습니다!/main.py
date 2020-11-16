from sys import stdin

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
        parents[island_2] = island_1

    roots = set()
    for island in parents[1:]:
        roots.add(find(island, parents))

    print(' '.join(map(str, list(roots))))

if __name__ == '__main__':
    main()