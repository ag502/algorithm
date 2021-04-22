from sys import stdin, exit

stdin = open("./input.txt", "r")
length_of_digit = int(stdin.readline())

number = ''


def is_good_seq(digit):
    for i in range(len(digit) // 2):
        right_sub_str = digit[len(digit) - 1 - i:]
        left_sub_str = digit[len(digit) - 2 - 2 * i:len(digit) - i - 1]

        if left_sub_str == right_sub_str:
            return False
    return True


def back_tracking(cur_number):
    global number
    number += str(cur_number)

    for next_number in range(1, 4):
        is_good = is_good_seq(number + str(next_number))
        if is_good and cur_number != next_number and len(number) < length_of_digit:
            back_tracking(next_number)

    if len(number) == length_of_digit:
        print(number)
        exit(0)

    number = number[:len(number) - 1]


def main():
    global number
    for cur_number in range(1, 4):
        back_tracking(cur_number)


if __name__ == '__main__':
    main()