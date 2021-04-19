from sys import stdin
from copy import deepcopy

stdin = open("./input.txt", "r")
num_of_eggs = int(stdin.readline())

eggs = []
for _ in range(num_of_eggs):
    eggs.append(list(map(int, stdin.readline().split())))


def dfs(egg1, egg2):
    if egg1 != 0 and egg2 != 0:
        egg1_info = eggs[egg1]
        egg2_info = eggs[egg2]
        egg1_info[0] -= egg2_info[1]
        egg2_info[0] -= egg1_info[0]

    for next_egg2 in range(num_of_eggs):
        dfs(egg1 + 1, next_egg2)


def main():
    pass

