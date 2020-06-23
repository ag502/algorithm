from sys import stdin
import math

def get_number_of_digit(number):
    number_length = len(str(number))
    number_of_digit = 0
    for i in range(1, number_length + 1):
        if i == number_length:
            number_of_digit += (number - 10 ** (i - 1) + 1) * i
            break
        number_of_digit += (10 ** i - 10 ** (i - 1)) * i
    return number_of_digit

def get_number_from_digit(number):
    k = number
    i = 1
    while True:
        if k < (10 ** i - 10 ** (i - 1)) * i:
            break
        else:
            k = k - (10 ** i - 10 ** (i - 1)) * i
            i = i + 1
    return 10 ** (i - 1) + math.ceil(k / i) - 1



def main():
    n, k = map(int, stdin.readline().split())

    number_of_digit = get_number_of_digit(n)
    if number_of_digit < k:
        print(-1)
        return
    target_number = get_number_from_digit(k)
    number_of_digit_bef = get_number_of_digit(target_number - 1)

    print(str(target_number)[k - number_of_digit_bef - 1])


if __name__ == "__main__":
    main()
