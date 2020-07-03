from collections import deque

def solution(cache_size, cities):
    cache = deque(maxlen=cache_size)
    running_time = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            running_time += 1
        else:
            cache.append(city)
            running_time += 5

    return running_time