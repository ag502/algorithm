from sys import stdin

def main():
    n, k = map(int, stdin.readline().split())
    number = list(map(int, list(stdin.readline().rstrip())))
    answer = [0] * (n - k)

    pivot = -1
    for i in range(n - k - 1, -1, -1):
        max_number = max(number[pivot + 1: n - i])
        pivot = number.index(max_number)

        if i == n - k - 1:
            for j in range(0, pivot + 1):
                number[j] = -1
        else:
            number[pivot] = -1

        answer[n - k - 1 - i] = str(max_number)

    print(''.join(answer))

if __name__ == '__main__':
    main()