from sys import stdin

def main():
    n = int(stdin.readline())
    plus_digit_array = []
    minus_digit_array = []
    zero_digit_array = []

    for _ in range(n):
        number = int(stdin.readline())
        if number > 0:
            plus_digit_array.append(number)
        elif number < 0:
            minus_digit_array.append(number)
        else:
            zero_digit_array.append(number)
    total_number_array = sorted(plus_digit_array, reverse=True) + sorted(minus_digit_array) + zero_digit_array


    pointer = 0
    max_sum = 0
    while True:
        if pointer >= len(total_number_array):
            break

        current_number = total_number_array[pointer]
        if pointer != len(total_number_array) - 1:
            next_number = total_number_array[pointer + 1]

            if current_number < current_number * next_number:
                max_sum += current_number * next_number
                pointer += 2
            else:
                max_sum += current_number
                pointer += 1

        else:
            max_sum += current_number
            pointer += 1

    print(max_sum)

if __name__ == "__main__":
    main()

