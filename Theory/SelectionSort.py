def selection_sort(array):
    for i in range(0, len(array)):
        min_index = i
        for j in range(i, len(array)):
            if (array[j] < array[min_index]):
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
        print(array)

    return array


print(selection_sort([1, 2, 7, 4, 6, 9, 5]))
