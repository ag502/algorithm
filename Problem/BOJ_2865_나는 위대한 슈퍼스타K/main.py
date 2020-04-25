from sys import stdin

def main():
    n, m, k = list(map(int, stdin.readline().split()))
    score_per_person = {}

    for _ in range(m):
        one_genre = list(stdin.readline().split())
        for index in range(0, len(one_genre), 2):
            if int(one_genre[index]) not in score_per_person:
                score_per_person[int(one_genre[index])] = []

            score_per_person[int(one_genre[index])].append(float(one_genre[index + 1]))

    max_score = []
    for participant in score_per_person:
        max_score.append(max(score_per_person[participant]))

    max_score.sort(reverse=True)
    print(max_score)
    print(score_per_person)

    result = 0
    for i in range(0, k):
        result += max_score[i]

    print("%0.1f" % result)

if __name__ == "__main__":
    main()