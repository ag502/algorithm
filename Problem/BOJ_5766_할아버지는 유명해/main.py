from sys import stdin


def main():
    stdin = open("./input.txt", "r")

    while True:
        num_of_week, num_of_people = map(int, stdin.readline().split())

        if num_of_week == 0 and num_of_people == 0:
            return

        ranks = {}

        for _ in range(num_of_week):
            people = list(map(int, stdin.readline().split()))
            for person in people:
                if person in ranks:
                    ranks[person] += 1
                else:
                    ranks[person] = 1

        ranks = list(ranks.items())
        ranks.sort(key=lambda x: (-x[1], x[0]))

        second_person_score = ranks[1][1]
        answer = []
        for person, score in ranks:
            if score == second_person_score:
                answer.append(str(person))

        print(' '.join(answer))


if __name__ == '__main__':
    main()