from sys import stdin


def average(array):
    print(round(sum(array) / len(array)))


def middle_value(array):
    print(array[(len(array) - 1) // 2])


def frequent_value(dicts):
    value = -4001
    time = 0
    found_time = 0

    for number, times in dicts:
        if time < times:
            value = number
            time = times
            found_time = 1
        elif time == times and found_time != 2:
            value = number
            found_time = 2

    print(value)


def number_range(array):
    max_value = max(array)
    min_value = min(array)

    print(max_value - min_value)


def main():
    num_of_number = int(stdin.readline())

    number_dict = {}
    number_array = []

    for _ in range(num_of_number):
        number = int(stdin.readline())
        number_array.append(number)

        if number in number_dict:
            number_dict[number] = number_dict[number] + 1
        else:
            number_dict[number] = 1

    number_dict = sorted(number_dict.items())
    number_array = sorted(number_array)

    average(number_array)
    middle_value(number_array)
    frequent_value(number_dict)
    number_range(number_array)


if __name__ == "__main__":
    main()