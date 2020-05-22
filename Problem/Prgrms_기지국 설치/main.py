import math

def solution(n, stations, w):
    answer = 0
    installed_site = []
    for building in stations:
        start_building = building - w
        end_building = building + w

        if start_building < 1:
            start_building = 1
        if end_building > n:
            end_building = n

        installed_site.append((start_building, end_building))
    for index in range(0, len(installed_site) - 1):
        current_building = installed_site[index]
        next_building = installed_site[index + 1]
        if next_building[0] - current_building[1] > 1 :
            answer += math.ceil((next_building[0] - 1 - current_building[1]) / (2 * w + 1))

    answer += math.ceil((installed_site[0][0] - 1) / (2 * w + 1))
    answer += math.ceil((n - installed_site[-1][-1]) / (2 * w + 1))
    return answer

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))

