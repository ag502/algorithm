from sys import stdin, maxsize
from math import floor


def is_valid(velocities, cur_velocity):
    for velocity in velocities:
        if cur_velocity < velocity:
            return False
        else:
            cur_velocity = velocity * floor(cur_velocity / velocity)
    return True


def search_velocity(velocities):
    start_velocity = max(velocities)
    end_velocity = maxsize

    while start_velocity <= end_velocity:
        mid_velocity = (start_velocity + end_velocity) // 2
        if is_valid(velocities, mid_velocity):
            end_velocity = mid_velocity - 1
        else:
            start_velocity = mid_velocity + 1
    return start_velocity


def main():
    stdin = open('./input.txt', 'r')
    num_of_planets = int(stdin.readline())
    required_velocity = list(map(int, stdin.readline().split()))

    min_velocity = search_velocity(required_velocity)
    print(min_velocity)


if __name__ == '__main__':
    main()