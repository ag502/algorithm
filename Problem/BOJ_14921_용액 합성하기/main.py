from sys import stdin, maxsize


def main():
    stdin = open('./input.txt', 'r')

    num_of_liquids = int(stdin.readline())
    liquids = list(map(int, stdin.readline().split()))
    liquids.sort()

    sum_of_two_liquids = maxsize
    start = first_liquid = 0
    end = second_liquid = len(liquids) - 1

    while start < end:
        result = liquids[start] + liquids[end]
        if sum_of_two_liquids > abs(result):
            sum_of_two_liquids = abs(result)
            first_liquid = liquids[start]
            second_liquid = liquids[end]

        if result <= 0:
            start += 1
        else:
            end -= 1

    print(first_liquid + second_liquid)


if __name__ == '__main__':
    main()
