from sys import stdin

def main():
    n = int(stdin.readline())
    resorts = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

    sort_by_distance = sorted(resorts, key=lambda x: (-x[0], x[1]))
    sort_by_cost = sorted(resorts, key=lambda x: -x[1])

    if len(resorts) == 1:
        print(1)
        return

    answer = set([])
    for i in range(0, n - 1):
        is_candidate = True
        for j in range(i + 1, n):
            if sort_by_distance[i][0] == sort_by_distance[j][0] and sort_by_distance[i][1] != sort_by_distance[j][1]:
                is_candidate = False
                break
            if sort_by_distance[i][0] != sort_by_distance[j][0] and sort_by_distance[i][1] == sort_by_distance[j][1]:
                is_candidate = False
                break
            if sort_by_distance[i][1] > sort_by_distance[j][1]:
                is_candidate = False
                break
        if is_candidate:
            answer.add(sort_by_distance[i])

    for i in range(0, n -1):
        is_candidate = True
        for j in range(i + 1, n):
            if sort_by_cost[i][1] == sort_by_cost[j][1] and sort_by_cost[i][0] != sort_by_cost[j][0]:
                is_candidate = False
                break
            if sort_by_cost[i][1] != sort_by_cost[j][1] and sort_by_cost[i][0] == sort_by_cost[j][0]:
                is_candidate = False
                break
            if sort_by_cost[i][0] > sort_by_cost [j][0]:
                is_candidate = False
                break
        if is_candidate:
            answer.add(sort_by_cost[i])

    print(len(answer))

if __name__ == "__main__":
    main()