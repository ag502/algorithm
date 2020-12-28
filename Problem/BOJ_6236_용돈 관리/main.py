from sys import stdin, maxsize


def main():
    stdin = open('./input.txt', 'r')
    days, num_of_withdraws = map(int, stdin.readline().split())
    expenses = [0] * days

    for idx in range(days):
        expenses[idx] = int(stdin.readline())

    start = max(expenses)
    end = maxsize
    while start <= end:
        mid = (start + end) // 2
        count = 0
        sum_of_expenses = 0

        for day in range(days):
            if sum_of_expenses + expenses[day] > mid:
                count += 1
                sum_of_expenses = 0
            sum_of_expenses += expenses[day]

        if sum_of_expenses != 0:
            count += 1

        if count <= num_of_withdraws:
            end = mid - 1
        else:
            start = mid + 1

    print(start)


if __name__ == '__main__':
    main()