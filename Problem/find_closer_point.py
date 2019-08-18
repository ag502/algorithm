from math import sqrt
import sys


def distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def closest_pair(tubles_array):
    result_distance = sys.maxsize
    point_list = []
    for i in range(len(tubles_array) - 1):
        for j in range(i + 1, len(tubles_array)):
            if result_distance > distance(tubles_array[i], tubles_array[j]):
                result_distance = distance(tubles_array[i], tubles_array[j])
                point_list = [tubles_array[i], tubles_array[j]]
    return point_list


test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))
