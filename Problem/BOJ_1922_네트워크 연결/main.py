from sys import stdin

stdin = open("./input.txt", "r")
num_of_computers = int(stdin.readline())
num_of_relations = int(stdin.readline())

edges = []
for _ in range(num_of_relations):
    pc_1, pc_2, cost = map(int, stdin.readline().split())
    edges.append((pc_1, pc_2, cost))

edges.sort(key=lambda x: x[2])
parents = [i for i in range(num_of_computers + 1)]


def find(computer):
    if computer == parents[computer]:
        return computer
    parents[computer] = find(parents[computer])
    return parents[computer]


def merge(computer_1, computer_2):
    computer_1_parent = find(computer_1)
    computer_2_parent = find(computer_2)

    if computer_1_parent == computer_2_parent:
        return
    parents[computer_2_parent] = computer_1_parent


def main():
    answer = 0
    for computer_1, computer_2, network_cost in edges:
        if find(computer_1) == find(computer_2):
            continue
        merge(computer_1, computer_2)
        answer += network_cost

    print(answer)


if __name__ == '__main__':
    main()