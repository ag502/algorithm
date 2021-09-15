from sys import stdin, maxsize

def selection_sort(array):
    for i in range(len(array)):
        min_value = maxsize
        min_idx = i
        for j in range(i, len(array)):
            if min_value > array[j]:
                min_value = array[j]
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

def main():
    stdin = open("Problem\grm_1I\input.txt", "r")
    num_of_data = int(stdin.readline())
    data = list(map(int, stdin.readline().split()))

    selection_sort(data)
    print(' '.join(map(str, data)))

if __name__ == "__main__":
    main()