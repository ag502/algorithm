from sys import stdin

def main():
    stdin = open('./input.txt', 'r')
    length_of_array, divisor = map(int, stdin.readline().split())
    array = list(map(int, stdin.readline().split()))

    array.sort()

    answer = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            answer_1 = array[i] // divisor
            answer_2 = array[j] // divisor

            if answer_1 == answer_2:
                answer += 1
            elif answer_2 > answer_1:
                break
    print(answer)

if __name__ == '__main__':
    main()
