from sys import stdin


def find(parents, person):
    if parents[person] == person:
        return person
    parents[person] = find(parents, parents[person])
    return parents[person]


def merge(parents, size, person_1, person_2):
    person_1_parent = find(parents, person_1)
    person_2_parent = find(parents, person_2)

    if person_1_parent == person_2_parent:
        return
    parents[person_2_parent] = person_1_parent
    size[person_1_parent] += size[person_2_parent]


def main():
    stdin = open("./input.txt", "r")
    test_case = int(stdin.readline())

    for _ in range(test_case):
        num_of_relations = int(stdin.readline())
        parents = {}
        size = {}

        for _ in range(num_of_relations):
            person_1, person_2 = stdin.readline().split()
            if person_1 not in parents:
                parents[person_1] = person_1
            if person_2 not in parents:
                parents[person_2] = person_2

            if person_1 not in size:
                size[person_1] = 1
            if person_2 not in size:
                size[person_2] = 1

            merge(parents, size, person_1, person_2)
            print(size[find(parents, person_1)])


if __name__ == '__main__':
    main()