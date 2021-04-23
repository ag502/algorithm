from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    target = int(stdin.readline())

    count = 1
    sum_of_num = 1
    cur_num = 1

    while sum_of_num <= target:
        cur_num += 1
        sum_of_num += cur_num
        count += 1

    print(count - 1)


if __name__ == '__main__':
    main()