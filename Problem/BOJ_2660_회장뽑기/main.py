from sys import stdin

INF = float('inf')

def main():
    stdin = open('./input.txt', 'r')
    num_of_members = int(stdin.readline())

    relations = [[INF] * (num_of_members + 1) for _ in range(num_of_members + 1)]
    for i in range(1, num_of_members + 1):
        relations[i][i] = 0

    while True:
        member_1, member_2 = map(int, stdin.readline().split())
        if member_1 == -1 and member_2 == -1:
            break
        relations[member_1][member_2] = 1
        relations[member_2][member_1] = 1

    for k in range(1, num_of_members + 1):
        for i in range(1, num_of_members + 1):
            if relations[i][k] == INF:
                continue
            for j in range(1, num_of_members + 1):
                relations[i][j] = min(relations[i][j], relations[i][k] + relations[k][j])

    scores = cal_score(relations)
    scores.sort(key=lambda x: x[1])
    min_score = scores[0][1]

    candidates = []
    for member, score in scores:
        if score == min_score:
            candidates.append(member)
    candidates.sort()

    print('{} {}'.format(min_score, len(candidates)))
    print(' '.join(map(str, candidates)))

def cal_score(relations):
    result = []
    for member, relation in enumerate(relations[1:]):
        result.append([member + 1, max(relation[1:])])

    return result

if __name__ == '__main__':
    main()