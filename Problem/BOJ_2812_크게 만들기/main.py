from sys import stdin
from itertools import combinations


def main():
    n, k = map(int, stdin.readline().split())
    number = stdin.readline().rstrip()

    number_list = list(number)
    current_number = int(''.join(number_list[:n - k]))

    for i in range(n - k, n):
        number_comb = combinations(list(str(current_number)), n - k - 1)
        for comb in number_comb:
            if current_number < int(''.join(comb) + number[i]):
                current_number = int(''.join(comb) + number[i])

    print(current_number)


if __name__ == '__main__':
    main()
