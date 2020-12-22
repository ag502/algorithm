from sys import stdin

def main():
    stdin = open('./input.txt', 'r')
    n = int(stdin.readline())
    m = int(stdin.readline())
    array = list(map(int, stdin.readline().split()))

    array.sort()

    num_of_armor = 0
    start = 0
    end = len(array) - 1

    while start < end:
        sum_of_gradient = array[start] + array[end]
        if sum_of_gradient < m:
            start += 1
        elif sum_of_gradient > m:
            end -= 1
        else:
            num_of_armor += 1
            start += 1
            end -= 1

    print(num_of_armor)

if __name__ == '__main__':
    main()