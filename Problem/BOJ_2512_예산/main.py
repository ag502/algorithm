from sys import stdin


def main():
    num_of_province = int(stdin.readline())
    budgets = list(map(int, stdin.readline().split()))
    total_budget = int(stdin.readline())

    candidate_ceiling = []

    start = 0
    end = max(budgets)

    while start <= end:
        mid = (start + end) // 2
        sum_of_budget = sum([budget if budget <=
                             mid else mid for budget in budgets])

        if sum_of_budget == total_budget:
            print(mid)
            return
        elif sum_of_budget < total_budget:
            candidate_ceiling.append(mid)
            start = mid + 1
        else:
            end = mid - 1

    print(max(candidate_ceiling))


if __name__ == "__main__":
    main()
