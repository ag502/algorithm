from sys import stdin


def main():
    stdin = open('./input.txt', 'r')
    num_of_gradient = int(stdin.readline())
    target_number = int(stdin.readline())
    gradient = list(map(int, stdin.readline().split()))

    gradient.sort()

    start = 0
    end = len(gradient) - 1
    answer = 0
    while start < end:
        cur_target = gradient[start] + gradient[end]
        if target_number > cur_target:
            start += 1
        elif target_number < cur_target:
            end -= 1
        else:
            answer += 1
            start += 1
            end -= 1

    print(answer)


if __name__ == '__main__':
    main()