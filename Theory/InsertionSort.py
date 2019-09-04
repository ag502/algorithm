def selection_sort(array):
    for i in range(0, len(array) - 1):
        j = i + 1
        move_num = array[j]
        for k in range(j - 1, -1, -1):
            if (move_num < array[k]):
                array[k + 1] = array[k]
                if (k == 0):
                    array[k] = move_num
            else:
                array[k + 1] = move_num
                break
        print(array)

    return array


print(selection_sort([5, 4, 3, 8, 9, 2]))
