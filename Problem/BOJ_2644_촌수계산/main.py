from sys import stdin
from collections import deque

def main():
    # file = open('./test_case.txt', 'r')

    num_of_family = int(stdin.readline())
    target_fam_1, target_fam_2 = map(int, stdin.readline().split())
    num_of_rel = int(stdin.readline())

    relations = {}
    for i in range(1, num_of_family + 1):
        relations[i] = []

    pq = deque()
    dist = [float('inf')] * (num_of_family + 1)

    for _ in range(num_of_rel):
        fam_1, fam_2 = map(int, stdin.readline().split())
        relations[fam_1].append(fam_2)
        relations[fam_2].append(fam_1)

    pq.append([target_fam_1, 0])
    dist[target_fam_1] = 0

    while len(pq) != 0:
        cur_fam, cur_dist = pq.popleft()
        if cur_dist > dist[cur_fam]:
            continue

        # 주변 가족 탐색
        for next_fam in relations[cur_fam]:
            if dist[next_fam] > dist[cur_fam] + 1:
                pq.append([next_fam, dist[cur_fam] + 1])
                dist[next_fam] = dist[cur_fam] + 1

    print(dist[target_fam_2] if dist[target_fam_2] != float('inf') else -1)

if __name__ == '__main__':
    main()
