from sys import stdin


def main():
    stdin = open('./input.txt', 'r')
    test_case = int(stdin.readline())

    for _ in range(test_case):
        num_of_applicants = int(stdin.readline())
        score = {}
        for applicant in range(1, num_of_applicants + 1):
            score[applicant] = list(map(int, stdin.readline().split()))

        first_phase = sorted(score.items(), key=lambda x: (x[1][0]))
        second_phase = sorted(score.items(), key=lambda x: (x[1][1]))

        second_phase_rank = [0] * (num_of_applicants + 1)
        for idx, applicant_info in enumerate(second_phase):
            applicant, rank = applicant_info
            second_phase_rank[applicant] = idx + 1

        passed_applicant = set()
        passed_applicant.add(first_phase[0][0])
        passed_applicant.add(second_phase[0][0])

        print(first_phase)
        print(second_phase)
        print(second_phase_rank)

        for idx in range(1, len(first_phase)):
            cur_applicant = first_phase[idx][0]
            prev_applicant = first_phase[idx - 1][0]
            if second_phase_rank[cur_applicant] < second_phase_rank[prev_applicant]:
                passed_applicant.add(cur_applicant)

        print(passed_applicant)
        print(len(passed_applicant))


if __name__ == '__main__':
    main()