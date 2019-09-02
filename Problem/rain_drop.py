def trapping_rain(buildings):

    rain_sum = 0
    for i in range(1, len(buildings) - 1):
        left_max = 0
        right_max = 0
        for j in range(i - 1, -1, -1):
            if left_max < buildings[j]:
                left_max = buildings[j]
        for k in range(i + 1, len(buildings)):
            if right_max < buildings[k]:
                right_max = buildings[k]
        if (left_max <= buildings[i]) | (right_max <= buildings[i]):
            continue
        rain_sum += right_max - buildings[i] if right_max < left_max else left_max - buildings[i]
    return rain_sum


print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))