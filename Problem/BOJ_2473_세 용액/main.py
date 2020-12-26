from sys import stdin, maxsize


def binary_search(array, start_idx, target):
    start = start_idx
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start


def main():
    stdin = open('./input.txt', 'r')
    num_of_liquids = int(stdin.readline())
    liquids = list(map(int, stdin.readline().split()))

    liquids.sort()

    sum_of_three_liquids = maxsize
    first_liquid = second_liquid = third_liquid = 0
    for i in range(num_of_liquids - 2):
        for j in range(i + 1, num_of_liquids - 1):
            sum_of_two_liquids = liquids[i] + liquids[j]
            target_idx = binary_search(liquids, j + 1, -sum_of_two_liquids)

            prev_idx = target_idx - 1
            next_idx = target_idx + 1

            for idx in [prev_idx, target_idx, next_idx]:
                if j < idx < num_of_liquids and \
                        abs(sum_of_two_liquids + liquids[idx]) < sum_of_three_liquids:
                    sum_of_three_liquids = abs(sum_of_two_liquids + liquids[idx])
                    first_liquid = liquids[i]
                    second_liquid = liquids[j]
                    third_liquid = liquids[idx]

    print(first_liquid, second_liquid, third_liquid)


if __name__ == '__main__':
    main()
