from sys import stdin

def main():
    num_of_array, max_sum = list(map(int, stdin.readline().split()))

    array = list(map(int, stdin.readline().split()))

    total = 0

    for i in range(len(array) - 2):
        first = array[i]
        for j in range(i + 1, len(array) - 1):
            second = array[j]
            for k in range(j + 1, len(array)):
                third = array[k]

                temp = first + second + third

                if total < temp <= max_sum:
                    total = temp
    print(total)


if __name__ == "__main__":
    main()