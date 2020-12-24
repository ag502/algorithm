from sys import stdin

def lower_bound(array, start_idx, target):
    start = start_idx
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

def upper_bound(array, start_idx, target):
    start = start_idx
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start

def main():
    stdin = open('./input.txt', 'r')
    length_of_array, divisor = map(int, stdin.readline().split())
    array = list(map(int, stdin.readline().split()))

    array.sort()

    answer = 0
    for idx, num in enumerate(array):
        share = num // divisor
        start_idx = lower_bound(array, idx + 1, divisor * share)
        end_idx = upper_bound(array, idx + 1, (divisor * (share + 1)) - 1)

        answer += end_idx - start_idx

    print(answer)

if __name__ == '__main__':
    main()