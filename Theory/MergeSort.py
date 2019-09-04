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


print(combine([1], []))
print(combine([], [1]))
print(combine([2], [1]))
print(combine([1, 2, 3, 4], [5, 6, 7, 8]))
print(combine([5, 6, 7, 8], [1, 2, 3, 4]))
print(combine([4, 7, 8, 9], [1, 3, 6, 10]))
