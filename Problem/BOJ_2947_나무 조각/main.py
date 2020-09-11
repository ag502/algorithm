from sys import stdin

def swap(array, idx1, idx2):
    temp = array[idx1]
    array[idx1] = array[idx2]
    array[idx2] = temp

def main():
    sticks = list(map(int, stdin.readline().split()))

    for i in range(len(sticks) - 1, -1, -1):
        for j in range(0, i):
            if sticks[j] > sticks[j + 1]:
                swap(sticks, j, j + 1)
                print(' '.join(map(str, sticks)))


if __name__ == '__main__':
    main()