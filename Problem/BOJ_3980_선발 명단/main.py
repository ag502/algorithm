from sys import stdin

stdin = open("./input.txt", "r")
test_case = int(stdin.readline())

player_ability = []
sum_of_ability = 0
answer = 0


def dfs(cur_player, position, visited, temp):
    global sum_of_ability, answer
    visited[cur_player] = True
    temp.append(str(cur_player))
    sum_of_ability += player_ability[cur_player][position]

    for next_player in range(11):
        if not visited[next_player] and len(temp) != 11:
            if player_ability[next_player][position + 1] != 0:
                dfs(next_player, position + 1, visited, temp)

    if len(temp) == 11:
        answer = max(answer, sum_of_ability)

    temp.pop()
    visited[cur_player] = False
    sum_of_ability -= player_ability[cur_player][position]


def main():
    global player_ability, sum_of_ability, answer
    for _ in range(test_case):
        player_ability.clear()
        answer = 0
        for _ in range(11):
            player_ability.append(list(map(int, stdin.readline().split())))

        for cur_player in range(11):
            visited = [False] * 11
            sum_of_ability = 0
            if player_ability[cur_player][0] != 0:
                dfs(cur_player, 0, visited, [])
        print(answer)


if __name__ == '__main__':
    main()