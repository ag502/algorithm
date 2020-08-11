from sys import stdin


def main():
    N = int(stdin.readline())
    nums = [i for i in range(0, N + 1)]

    for i in range(2, int(N ** 0.5) + 1):
        current_num = nums[i]
        for j in range(2, N // current_num + 1):
            nums[current_num * j] = -1

    prime = []
    for num in nums:
        if num != 0 and num != 1 and num != -1:
            prime.append(num)
    prime += [0]
    # print(prime)

    low = high = 0
    sum_of_num = prime[low]
    answer = 0

    while high < len(prime) - 1:
        if sum_of_num == N:
            answer += 1
            sum_of_num -= prime[low]
            low += 1
        elif sum_of_num > N:
            sum_of_num -= prime[low]
            low += 1
        else:
            high += 1
            sum_of_num += prime[high]

    print(answer)


if __name__ == "__main__":
    main()
