from sys import stdin

def bubble_sort(array, length):
    for i in range(length - 2):
        for j in range(length - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def main():
    stdin = open('Problem\grm_2G\input.txt', 'r')
    num_of_data = int(stdin.readline())
    data = list(map(int, stdin.readline().split()))

    bubble_sort(data, num_of_data)

    print(' '.join(map(str, data)))

if __name__ == "__main__":
    main()