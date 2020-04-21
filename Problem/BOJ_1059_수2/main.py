from sys import stdin


def main():
    l = int(stdin.readline())
    lucky_set = list(map(int, stdin.readline().split()))
    n = int(stdin.readline())

    lucky_set.sort()

    start_range = 0
    end_range = 0
    if n > lucky_set[len(lucky_set) - 1]:
        print(0)
        return
    for index in range(0, len(lucky_set)):
        if n < lucky_set[index]:
            if index == 0:
                start_range = 1
                end_range = lucky_set[index] - 1
                break
            start_range = lucky_set[index - 1] + 1
            end_range = lucky_set[index] - 1
            break
        elif n == lucky_set[index]:
            print(0)
            return

    if start_range >= end_range:
        print(0)
        return
    else:
        # count = 0
        # range_arr = [number for number in range(start_range, end_range + 1)]
        # for i in range(len(range_arr) - 1):
        #     for j in range(i + 1, len(range_arr)):
        #         if range_arr[i] <= n <= range_arr[j]:
        #             count += 1
        number_of_range = end_range - start_range + 1
        has_number = (number_of_range * (number_of_range - 1) // 2) \
                     - ((number_of_range - 1) * (number_of_range - 2) // 2)
        include_number = (n - start_range) * (end_range - n)
        print(has_number + include_number)


if __name__ == "__main__":
    main()