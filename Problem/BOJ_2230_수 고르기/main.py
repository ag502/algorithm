from sys import stdin, maxsize

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

def main():
    stdin = open('./input.txt', 'r')
    length_of_seq, diff = map(int, stdin.readline().split())

    sequence = [0] * length_of_seq
    for idx in range(length_of_seq):
        sequence[idx] = int(stdin.readline())

    sequence.sort()

    difference = maxsize
    for idx, num in enumerate(sequence):
        target_idx = lower_bound(sequence, idx, diff + num)
        if idx <= target_idx < length_of_seq:
            difference = min(difference, sequence[target_idx] - sequence[idx])
    print(difference)

if __name__ == '__main__':
    main()