from sys import stdin

def main():
    stdin = open('./input.txt', 'r')
    num_of_number = int(stdin.readline())

    sequence = [0] + list(map(int, stdin.readline().split()))

    acc_sequence = [0] * len(sequence)
    for idx, number in enumerate(sequence):
        if idx == 0:
            acc_sequence[idx] = number
        else:
            acc_sequence[idx] = acc_sequence[idx - 1] + number

    num_of_range = int(stdin.readline())
    for _ in range(num_of_range):
        i, j = map(int, stdin.readline().split())
        print(acc_sequence[j] - acc_sequence[i - 1])

if __name__ == '__main__':
    main()