from sys import stdin, maxsize


class Main:
    def __init__(self):
        self.num_of_player = 0
        self.ability = []
        self.players = set()
        self.teams = []
        self.ability_diff = maxsize

        self.main()

    def compose_team(self, cur_player, count, cur_team=set()):
        cur_team.add(cur_player)

        if len(cur_team) < count:
            for next_player in range(cur_player + 1, self.num_of_player):
                self.compose_team(next_player, count, cur_team)
        elif len(cur_team) == count:
            self.teams.append([cur_team.copy(), self.players - cur_team])

        cur_team.remove(cur_player)

    def calc_ability(self, team_case):
        start_team, link_team = team_case

        start_team_ability = 0
        start_team = list(start_team)

        for i in range(len(start_team) - 1):
            for j in range(i, len(start_team)):
                player_1 = start_team[i]
                player_2 = start_team[j]
                start_team_ability += self.ability[player_1][player_2] + self.ability[player_2][player_1]

        link_team_ability = 0
        link_team = list(link_team)

        for i in range(len(link_team) - 1):
            for j in range(i, len(link_team)):
                player_1 = link_team[i]
                player_2 = link_team[j]
                link_team_ability += self.ability[player_1][player_2] + self.ability[player_2][player_1]

        # print(start_team_ability, link_team_ability)
        return abs(start_team_ability - link_team_ability)

    def main(self):
        stdin = open("./input.txt", "r")
        self.num_of_player = int(stdin.readline())
        for _ in range(self.num_of_player):
            self.ability.append(list(map(int, stdin.readline().split())))

        for player in range(self.num_of_player):
            self.players.add(player)

        for count in range(1, (self.num_of_player // 2) + 1):
            for start_player in range(self.num_of_player):
                self.compose_team(start_player, count)

        for team_case in self.teams:
            self.ability_diff = min(self.ability_diff, self.calc_ability(team_case))

        print(self.ability_diff)


if __name__ == '__main__':
    Main()