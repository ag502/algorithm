from sys import stdin

parents = [i for i in range((10 ** 6) + 1)]
size = [1] * ((10 ** 6) + 1)


def find(part):
    if part == parents[part]:
        return part
    parents[part] = find(parents[part])
    return parents[part]


def merge(part1, part2):
    part1_parent = find(part1)
    part2_parent = find(part2)

    if part1_parent == part2_parent:
        return
    parents[part2_parent] = part1_parent
    size[part1_parent] += size[part2_parent]


def main():
    stdin = open("./input.txt", "r")
    num_of_instructions = int(stdin.readline())

    for _ in range(num_of_instructions):
        info = stdin.readline().split()
        if info[0] == "I":
            merge(int(info[1]), int(info[2]))

        if info[0] == "Q":
            parent = find(int(info[1]))
            print(size[parent])


if __name__ == '__main__':
    main()