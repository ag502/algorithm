from sys import stdin

def main():
    stdin = open('./input.txt', 'r')
    n = int(stdin.readline())
    m = int(stdin.readline())
    array = list(map(int, stdin.readline().split()))

    array.sort()

    num_of_armor = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            sum_of_gradient = array[i] + array[j]
            if sum_of_gradient == m:
                num_of_armor += 1
            elif sum_of_gradient > m:
                break
    print(num_of_armor)

if __name__ == '__main__':
    main()