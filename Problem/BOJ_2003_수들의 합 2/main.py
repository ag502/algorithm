from sys import stdin


def main():
    N, M = map(int, stdin.readline().split())
    nums = list(map(int, stdin.readline().split())) + [0]

    low = high = 0
    answer = 0
    sum_of_number = nums[low]

    while high < N:
        if sum_of_number == M:
            answer += 1
            sum_of_number -= nums[low]
            low += 1
        elif sum_of_number > M:
            sum_of_number -= nums[low]
            low += 1
        else:
            high += 1
            sum_of_number += nums[high]
    print(answer)


if __name__ == "__main__":
    main()
