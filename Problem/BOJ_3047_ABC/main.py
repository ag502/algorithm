from sys import stdin


def main():
    number_array = list(map(int, stdin.readline().split()))
    print_order = stdin.readline().rstrip()
    number_array.sort()

    number_dict_with_tag = {'A': number_array[0], 'B': number_array[1], 'C': number_array[2]}

    result = ''

    for order in print_order:
        result += str(number_dict_with_tag[order]) + ' '

    print(result.strip())


if __name__ == "__main__":
    main()