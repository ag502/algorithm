def merge(left_list, right_list):
    new_list = []
    left_ptr = 0
    right_ptr = 0
    while left_ptr < len(left_list) and right_ptr < len(right_list):
        if left_list[left_ptr] >= right_list[right_ptr]:
            new_list.append(right_list[right_ptr])
            right_ptr += 1
        elif left_list[left_ptr] < right_list[right_ptr]:
            new_list.append(left_list[left_ptr])
            left_ptr += 1

    if left_ptr >= len(left_list):
        new_list = new_list + right_list[right_ptr:]
    elif right_ptr >= len(right_list):
        new_list = new_list + left_list[left_ptr:]

    return new_list

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    return merge(merge_sort(input_list[0:len(input_list) // 2]),
                 merge_sort(input_list[len(input_list) // 2:]))



print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([21, 10, 12, 20, 25, 13, 15, 22]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
