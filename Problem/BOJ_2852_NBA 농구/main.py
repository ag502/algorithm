from sys import stdin

def convert_minute_to_second(time):
    minute, second = time.split(":")
    return 60 * int(minute) + int(second)

def convert_second_to_minute(time):
    minute = time // 60
    second = time % 60

    minute = '0' + str(minute) if 0 <= minute < 10 else str(minute)
    second = '0' + str(second) if 0 <= second < 10 else str(second)

    return minute + ":" + second

def get_winning_time(goal_info):
    is_team1_winning, is_team2_winning = [False, False]
    team1_winning_time, team2_winning_time = [0, 0]
    begin_time = 0
    for scores, time in goal_info:
        team1_score, team2_score = scores

        if team1_score > team2_score:
            if not is_team1_winning:
                is_team1_winning = True
                begin_time = time
        elif team1_score < team2_score:
            if not is_team2_winning:
                is_team2_winning = True
                begin_time = time

        if team1_score == team2_score:
            if is_team1_winning:
                team1_winning_time += time - begin_time
                is_team1_winning = False
            elif is_team2_winning:
                team2_winning_time += time - begin_time
                is_team2_winning = False

    if is_team1_winning:
        team1_winning_time += 60 * 48 - begin_time
    elif is_team2_winning:
        team2_winning_time += 60 * 48 - begin_time

    return team1_winning_time, team2_winning_time


def main():
    stdin = open('./test_case.txt', 'r')
    goal_of_num = int(stdin.readline())

    num_of_goal_team1 = 0
    num_of_goal_team2 = 0
    goal_info = []

    for _ in range(goal_of_num):
        team, time = stdin.readline().split()
        if team == "1":
            num_of_goal_team1 += 1
        elif team == "2":
            num_of_goal_team2 += 1
        goal_info.append(([num_of_goal_team1, num_of_goal_team2], convert_minute_to_second(time)))

    team1_winning_time, team2_winning_time = get_winning_time(goal_info)

    # print(team1_winning_time, team2_winning_time)

    for time in [team1_winning_time, team2_winning_time]:
        print(convert_second_to_minute(time))

if __name__ == '__main__':
    main()