from sys import stdin
from collections import Counter

def main():
    n = int(stdin.readline())
    location = list([ tuple(stdin.readline().split()) for _ in range(n)])
    location.sort(key=lambda x: x)

    location_x = []
    location_y = []

    for x, y in location:
        location_x.append(x)
        location_y.append(y)

    counter_x = Counter(location_x)
    counter_y = Counter(location_y)

    sum_loc = 0
    for x in counter_x:
        if counter_x[x] >= 2:
            sum_loc += 1

    for y in counter_y:
        if counter_y[y] >= 2:
            sum_loc += 1

    print(sum_loc)


if __name__ == "__main__":
    main()