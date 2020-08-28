from sys import stdin


def main():
    N = int(stdin.readline().rstrip())
    ability = [[0] * (N + 1)]

    for _ in range(N):
        ability.append([0] + list(map(int, stdin.readline().split())))

    visited = [False] * (N + 1)
    people = set([i for i in range(1, N + 1)])

    team = []
    comb_team(1, N, N // 2, 0, visited, [], team)

    diff = 100
    for team1 in team:
        team2 = list(people - set(team1))

        s1 = 0
        s2 = 0
        for i in range(len(team1)):
            for j in range(len(team1)):
                if team1[i] != team1[j]:
                    s1 += ability[team1[i]][team1[j]]

                if team2[i] != team2[j]:
                    s2 += ability[team2[i]][team2[j]]
        if diff > abs(s1 - s2):
            diff = abs(s1 - s2)

    print(diff)


def comb_team(cur_per, n, m, selected_per, visited, answer, t):
    # 1. 체크인
    visited[cur_per] = True
    selected_per += 1
    # 2. 도착
    answer.append(cur_per)
    # 3. 가능한 사람 순회
    for next_per in range(cur_per + 1, n + 1):
        # 4. 가능성 검사
        if not visited[next_per] and selected_per != m:
            comb_team(next_per, n, m, selected_per, visited, answer, t)
    # 5. 체크아웃
    if len(answer) == m:
        t.append(answer[:])
    visited[cur_per] = False
    selected_per -= 1
    answer.pop()


if __name__ == "__main__":
    main()
