from sys import stdin

def main():
    stdin = open('./input.txt', 'r')
    length_of_array = int(stdin.readline())
    array = list(map(int, stdin.readline().split()))
    target_number = int(stdin.readline())

    array.sort()

    answer = 0
    start = 0
    end = len(array) - 1
    while start < end:
        sum_of_sub_array = array[start] + array[end]
        if sum_of_sub_array < target_number:
            start += 1
        elif sum_of_sub_array > target_number:
            end -= 1
        else:
            answer += 1
            start += 1
            end -= 1
    print(answer)

if __name__ == '__main__':
    main()