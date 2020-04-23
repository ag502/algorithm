from sys import stdin
from collections import Counter

def is_decreasing_number(number):
    if 0 <= number <= 9:
        return True

    # digit_array = list(map(int, str(number)))
    # for index in range(len(digit_array) - 1):
    #     if digit_array[index] - digit_array[index + 1] <= 0:
    #         return False
    # return True

    string_number = str(number)
    digit_counter = Counter(string_number).most_common(1)

    if digit_counter[0][1] > 1:
        return False

    sorted_string_number = sorted(string_number, reverse=True)

    if string_number == ''.join(sorted_string_number):
        return True
    else:
        return False


def main():
    n = int(stdin.readline())

    if n > 1023:
        print(-1)
        return

    count = 0
    number = 0
    while 1:
        print(number)
        if is_decreasing_number(number):
            count += 1
        if count == n :
            print(number)
            return
        number += 1

if __name__ == "__main__":
    main()
    # print(is_decreasing_number(9764320))