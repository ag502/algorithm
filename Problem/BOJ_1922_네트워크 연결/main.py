from sys import stdin


stdin = open("./input.txt", "r")
num_of_computer = int(stdin.readline())
num_of_relations = int(stdin.readline())

edges = []

for _ in range(num_of_relations):
    computer1, computer2, cost = map(int, stdin.readline().split())
    edges.append((computer1, computer2, cost))

edges.sort(key=lambda x: x[2])
parents = [i for i in range(num_of_computer + 1)]


def find(cur_pc):
    if cur_pc == parents[cur_pc]:
        return cur_pc
    parents[cur_pc] = find(parents[cur_pc])
    return parents[cur_pc]


def merge(pc1, pc2):
    pc1_parent = find(pc1)
    pc2_parent = find(pc2)

    if pc1_parent == pc2_parent:
        return
    parents[pc2_parent] = pc1_parent


def main():
    answer = 0
    for pc1, pc2, cost in edges:
        pc1_parent = find(pc1)
        pc2_parent = find(pc2)
        if pc1_parent == pc2_parent:
            continue
        merge(pc1, pc2)
        answer += cost

    print(answer)


if __name__ == '__main__':
    main()