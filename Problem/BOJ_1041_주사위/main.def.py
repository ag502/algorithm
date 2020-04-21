from sys import stdin


def main():
    n = int(stdin.readline())
    dice_number = list(map(int, stdin.readline().split()))
    dice_number.sort()

    total_sum = 0

    if n == 1:
        total_sum = sum(dice_number[:5])
    else:
        plain = n ** 2
        three_plain = 4
        one_plain = (n - 2) ** 2
        two_plain = plain - three_plain - one_plain

        front_back = (dice_number[0] * 4
                      + dice_number[0] * two_plain
                      + dice_number[0] * one_plain) * 2
        right_left = (dice_number[1] * 4
                      + dice_number[1] * two_plain // 2 + dice_number[0] * two_plain // 2
                      + dice_number[0] * one_plain) * 2
        top = (dice_number[2] * 4
               + dice_number[1] * two_plain // 2 + dice_number[1] * two_plain // 2
               + dice_number[0] * one_plain)

        total_sum = front_back + right_left + top

    print(total_sum)


if __name__ == "__main__":
    main()