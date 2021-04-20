from sys import stdin
from copy import deepcopy

stdin = open("./input.txt", "r")
num_of_eggs = int(stdin.readline())

eggs = []
for _ in range(num_of_eggs):
    eggs.append(list(map(int, stdin.readline().split())))


def dfs(egg1, egg2):
    egg1_origin_info = eggs[egg1][:]
    egg2_origin_info = eggs[egg2][:]
    print(egg1, egg2)

    eggs[egg1][0] -= eggs[egg2][1]
    eggs[egg2][0] -= eggs[egg1][1]

    for next_egg1 in range(egg1 + 1, num_of_eggs):
        if eggs[next_egg1][0] > 0:
            for next_egg2 in range(num_of_eggs):
                if eggs[next_egg2][0] > 0 and next_egg1 != next_egg2:
                    dfs(next_egg1, next_egg2)

    # if egg1 == num_of_eggs - 1:
    #     print(eggs)
    print(eggs)
    eggs[egg1] = egg1_origin_info
    eggs[egg2] = egg2_origin_info


def main():
    for egg2 in range(1, num_of_eggs):
        dfs(0, egg2)


if __name__ == '__main__':
    main()

