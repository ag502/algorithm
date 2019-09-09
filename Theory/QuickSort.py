def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def partition(my_list, start, end):
    index = start
    big_num = start
    pivot = end

    while index < end:
        if my_list[index] < my_list[pivot]:
            swap_elements(my_list, index, big_num)
            index += 1
            big_num += 1
        else:
            index += 1

    swap_elements(my_list, big_num, pivot)
    pivot = big_num

    return pivot


def quicksort(my_list, start, end):
    pivot = partition(my_list, start, end)
    if start == end:
        return
    if pivot + 1 > end:
        quicksort(my_list, start, pivot - 1)
    elif pivot - 1 < start:
        quicksort(my_list, pivot + 1, end)
    else:
        quicksort(my_list, start, pivot - 1)
        quicksort(my_list, pivot + 1, end)

    # if end - start < 1:
    #    return
    # pivot = partition(my_list, start, end)
    # quicksort(my_list, start, pivot - 1)
    # quicksort(my_list, pivot + 1, end)
    # return my_list

    return my_list


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)