from sys import stdin

def main():
    participants = int(stdin.readline())
    staffs = int(stdin.readline())
    score_per_staff = {}
    chips_per_staff = {}
    score_set = []

    for _ in range(staffs):
        name, num_of_votes = list(stdin.readline().split())
        num_of_votes = int(num_of_votes)

        if num_of_votes >= participants * 0.05:
            score_per_staff[name] = num_of_votes
            chips_per_staff[name] = 0

    for staff in score_per_staff:
        staff_score = score_per_staff[staff]
        temp = []
        for i in range(1, 15):
            temp.append(staff_score / i)
            score_set.append(staff_score / i)
        score_per_staff[staff] = temp

    score_set.sort(key=lambda x: -x)

    for i in range(14):
        current_score = score_set[i]
        for staff in score_per_staff:
            if current_score in score_per_staff[staff]:
                chips_per_staff[staff] += 1

    chips_per_staff = sorted(chips_per_staff.items(), key=lambda x: x[0])

    for staff, num_of_chips in chips_per_staff:
        res = '{} {}'.format(staff, num_of_chips)
        print(res)

if __name__ == "__main__":
    main()
