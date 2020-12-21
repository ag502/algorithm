from sys import stdin

def main():
    stdin = open('./input.txt', 'r')
    length_of_array, m = map(int, stdin.readline().split())
    array = list(map(int, stdin.readline().split())) + [0]

    num_of_case = 0
    sum_of_sub_array = 0
    start = end = 0
    while start <= end <= length_of_array:
        if sum_of_sub_array >= m:
            sum_of_sub_array -= array[start]
            start += 1
        else:
            sum_of_sub_array += array[end]
            end += 1

        if sum_of_sub_array == m:
            num_of_case += 1
    print(num_of_case)

if __name__ == '__main__':
    main()