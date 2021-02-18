from sys import stdin


# 왼쪽이 먼저 오면 -1, 같으면 0, 오른쪽이 먼저오면 1
def compare(elem1, elem2):
    if elem1[1] < elem2[1]:
        return -1
    elif elem1[1] > elem2[1]:
        return 1
    else:
        if elem1[0] < elem2[0]:
            return -1
        elif elem1[0] > elem2[0]:
            return 1
        return 0


def merge(array1, array2):
    new_array = []
    idx1 = 0
    idx2 = 0
    while idx1 < len(array1) and idx2 < len(array2):
        cur_elem1 = array1[idx1]
        cur_elem2 = array2[idx2]
        comparator = compare(cur_elem1, cur_elem2)
        if comparator == -1:
            new_array.append(cur_elem1)
            idx1 += 1
        elif comparator == 1:
            new_array.append(cur_elem2)
            idx2 += 1
        elif comparator == 0:
            new_array.append(cur_elem1)
            new_array.append(cur_elem2)
            idx1 += 1
            idx2 += 1

    if idx1 >= len(array1) and idx2 < len(array2):
        new_array += array2[idx2:]
    elif idx2 >= len(array2) and idx1 < len(array1):
        new_array += array1[idx1:]

    return new_array


def merge_sort(array):
    if len(array) == 1:
        return array
    return merge(merge_sort(array[:len(array) // 2]), merge_sort(array[len(array) // 2:]))


def main():
    stdin = open("./input.txt", "r")
    num_of_meetings = int(stdin.readline())
    meetings = []

    for _ in range(num_of_meetings):
        meetings.append(tuple(map(int, stdin.readline().split())))

    sort_meetings = merge_sort(meetings)

    answer = [sort_meetings[0]]
    for meeting in sort_meetings[1:]:
        if meeting[0] >= answer[len(answer) - 1][1]:
            answer.append(meeting)

    print(len(answer))


if __name__ == '__main__':
    main()