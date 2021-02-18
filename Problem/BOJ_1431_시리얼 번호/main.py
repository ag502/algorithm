from sys import stdin


# 왼쪽이 먼저 오면 true, 오른쪽이 먼저 오면 false
def compare(elem1, elem2):
    if len(elem1) < len(elem2):
        return True
    elif len(elem1) > len(elem2):
        return False
    else:
        sum1 = 0
        sum2 = 0
        for char1, char2 in zip(elem1, elem2):
            if ord('0') <= ord(char1) <= ord('9'):
                sum1 += int(char1)
            if ord('0') <= ord(char2) <= ord('9'):
                sum2 += int(char2)
        if sum1 < sum2:
            return True
        elif sum2 < sum1:
            return False

    if elem1 < elem2:
        return True
    elif elem2 < elem1:
        return False


def conquer(array1, array2):
    new_array = []
    idx1 = 0
    idx2 = 0

    while idx1 < len(array1) and idx2 < len(array2):
        cur_elem1 = array1[idx1]
        cur_elem2 = array2[idx2]

        if compare(cur_elem1, cur_elem2):
            new_array.append(cur_elem1)
            idx1 += 1
        else:
            new_array.append(cur_elem2)
            idx2 += 1

    if idx1 >= len(array1) and idx2 < len(array2):
        new_array += array2[idx2:]
    elif idx2 >= len(array2) and idx1 < len(array1):
        new_array += array1[idx1:]

    return new_array


def divide(array):
    if len(array) == 1:
        return array
    return conquer(divide(array[:len(array) // 2]), divide(array[len(array) // 2:]))


def main():
    stdin = open("./input.txt", "r")
    n = int(stdin.readline())
    strings = []

    for _ in range(n):
        strings.append(stdin.readline().rstrip())

    answer = divide(strings)

    for string in answer:
        print(string)


if __name__ == '__main__':
    main()