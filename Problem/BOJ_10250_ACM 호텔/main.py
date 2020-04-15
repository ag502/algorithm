from sys import stdin


def convert(number):
    if 0 < number < 10:
        return '0' + str(number)
    else:
        return str(number)


def main():
    test_case = int(stdin.readline())

    for _ in range(test_case):
        h, w, m = list(map(int, stdin.readline().split()))
        floor = m % h

        #나눌 때 배수 주의
        if floor == 0:
            floor = h
            room_number = convert(m // h)
        else:
            room_number = convert(m // h + 1)

        print(str(floor) + room_number)


if __name__ == "__main__":
    main()
