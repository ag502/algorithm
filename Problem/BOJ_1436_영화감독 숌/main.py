from sys import stdin


def main():
    N = int(stdin.readline().rstrip())

    count = 0
    answer = 0
    number = 666
    while count != N:
        if '666' in str(number):
            # print(i)
            answer = number
            count += 1
        number += 1

    print(answer)


if __name__ == "__main__":
    main()
