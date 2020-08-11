from sys import stdin


def main():
    N, S = map(int, stdin.readline().split())
    nums = list(map(int, stdin.readline().split())) + [0]

    min_length = 100000
    low = high = 0
    sum_of_num = nums[low]

    while high < N:
        if sum_of_num >= S:
            min_length = min(min_length, abs(high - low) + 1)
            sum_of_num -= nums[low]
            low += 1
        elif sum_of_num < S:
            high += 1
            sum_of_num += nums[high]

    print(min_length if min_length != 100000 else 0)


if __name__ == "__main__":
    main()
