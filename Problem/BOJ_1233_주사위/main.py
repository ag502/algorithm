from sys import stdin
from itertools import product
from collections import Counter


def main():
    s1, s2, s3 = map(int, stdin.readline().split())
    sum_count = []

    for dice_num in product(range(1, s1 + 1), range(1, s2 + 1), range(1, s3 + 1)):
        sum_count.append(sum(dice_num))

    sum_count = Counter(sum_count)
    print(sum_count.most_common()[0][0])


if __name__ == "__main__":
    main()
