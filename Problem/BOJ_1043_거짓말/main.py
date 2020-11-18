from sys import stdin

def find(parents, person):
    if parents[person] == person:
        return person
    parents[person] = find(parents, parents[person])
    return parents[person]

def merge(parents, truth_know_people, per1, per2):
    per1_root = find(parents, per1)
    per2_root = find(parents, per2)
    if per1_root == per2_root:
        return

    if per2_root in truth_know_people:
        parents[per1_root] = per2_root
    else:
        parents[per2_root] = per1_root

def main():
    stdin = open('./test_case.txt')
    n, m = map(int, stdin.readline().split())
    truth_know_people = list(map(int, stdin.readline().split()))[1:]

    parents = [i for i in range(n + 1)]

    for _ in range(m):
        participants = list(map(int, stdin.readline().split()))[1:]

        for idx in range(len(participants) - 1):
            merge(parents, truth_know_people, participants[idx], participants[idx + 1])

    # print(parents)
    if len(truth_know_people) == 0:
        print(m)
    else:
        answer = set()
        for person in parents[1:]:
            answer.add(find(parents, person))

        count = 0
        for person in answer:
            if person not in truth_know_people:
                count += 1
        print(count)


if __name__ == '__main__':
    main()