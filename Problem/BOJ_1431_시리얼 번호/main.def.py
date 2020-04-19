from sys import stdin


def sum_of_digits(number):
    digit_array = []
    for digit in number:
        try:
            digit_array.append(int(digit))
        except:
            pass

    sum = 0
    for i in range(len(digit_array)):
        sum += digit_array[i]

    return sum


def main():
    number_of_guitar = int(stdin.readline())

    serial_number = [stdin.readline().rstrip() for _ in range(number_of_guitar)]

    serial_number = sorted(serial_number, key=lambda x: (len(x), sum_of_digits(x), x))

    for serial in serial_number:
        print(serial)


if __name__ == "__main__":
    main()