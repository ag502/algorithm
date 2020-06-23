from sys import stdin
import math

def get_number_of_digit(number, number_length):
    number_of_digit = 0
    for i in range(1, number_length + 1):
        if i == number_length:
            number_of_digit += (number - 10 ** (i - 1) + 1) * i
            break
        number_of_digit += (10 ** i - 10 ** (i - 1)) * i

    return number_of_digit

def get_number_from_standard(k, number_length):
    answer = k
    for i in range(1, number_length + 1):
        if i == number_length:
            return 10 ** (number_length - 1) + math.ceil(answer / i) - 1
        answer -= (10 ** i - 10 ** (i - 1)) * i

def main():
    n, k = map(int, stdin.readline().split())
    number_length = len(str(n))

    number_of_digit = get_number_of_digit(n, number_length)
    if number_of_digit < k:
        print(-1)
        return

    target_number = get_number_from_standard(k, len(str(k)))
    number_of_digit = get_number_of_digit(target_number - 1, len(str(target_number - 1)))

    print(str(target_number)[k - number_of_digit - 1])

if __name__ == "__main__":
    main()

