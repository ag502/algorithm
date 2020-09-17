from sys import stdin

def main():
    N, M = map(int, stdin.readline().split())
    numbers = list(map(int, stdin.readline().split()))
    acc_sums = [0] * len(numbers)

    sum = 0
    for idx, number in enumerate(numbers):
        sum += number
        acc_sums[idx] = sum

    for _ in range(M):
        i, j = map(int, stdin.readline().split())
        if i == 1:
            print(acc_sums[j - 1])
        else:
            print(acc_sums[j - 1] - acc_sums[i - 2])

if __name__ == '__main__':
    main()