from sys import stdin


def main():
    stdin = open('./input.txt', 'r')
    num_of_traffic_lights, k, broken_traffic_lights = map(int, stdin.readline().split())

    traffic_lights = [1] * (num_of_traffic_lights + 1)
    for _ in range(broken_traffic_lights):
        traffic_lights[int(stdin.readline())] = 0

    start = 0
    end = broken_traffic_lights
    while start <= end:
        mid = (start + end) // 2
        if num_of_traffic_lights - broken_traffic_lights + mid >= k:
            end = mid - 1
        else:
            start = mid + 1
    print(start)


if __name__ == '__main__':
    main()
