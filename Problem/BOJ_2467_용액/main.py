from sys import stdin, maxsize

def main():
    stdin = open('./input.txt', 'r')
    num_of_liquids = int(stdin.readline())
    liquids = list(map(int, stdin.readline().split()))

    liquids.sort()

    start = liquid_1 = 0
    end = liquid_2 = len(liquids) - 1
    sum_of_liquid = maxsize
    while start < end:
        result = liquids[start] + liquids[end]
        if abs(result) < sum_of_liquid:
            sum_of_liquid = abs(result)
            liquid_1 = start
            liquid_2 = end
        if result <= 0:
            start += 1
        else:
            end -= 1

    print(' '.join(map(str, [liquids[liquid_1], liquids[liquid_2]])))

if __name__ == '__main__':
    main()