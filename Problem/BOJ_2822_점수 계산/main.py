from sys import stdin

def main():
    problem_list = [(i, int(stdin.readline())) for i in range(8)]
    problem_list = sorted(problem_list, key=lambda x:-x[1])

    sum_of_score = 0
    included_problem_list = []
    for i in range(5):
        sum_of_score += problem_list[i][1]
        included_problem_list.append(problem_list[i][0] + 1)

    included_problem_list.sort()
    included_problem = ''
    for score in included_problem_list:
        included_problem += str(score) + ' '

    print(sum_of_score)
    print(included_problem.strip())

if __name__ == '__main__':
    main()