def combine(list1, list2):
    new_list = []
    first_ptr = 0
    second_ptr = 0
    while (first_ptr < len(list1)) & (second_ptr < len(list2)):
        if list1[first_ptr] >= list2[second_ptr]:
            new_list.append(list2[second_ptr])
            second_ptr += 1
        else:
            new_list.append(list1[first_ptr])
            first_ptr += 1

    if first_ptr >= len(list1):
        new_list = new_list + list2[second_ptr:]
    elif second_ptr >= len(list2):
        new_list = new_list + list1[first_ptr:]

    return new_list


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    return combine(merge_sort(input_list[0:len(input_list) // 2]),
                   merge_sort(input_list[len(input_list) // 2:]))


print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
