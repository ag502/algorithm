from sys import stdin


def main():
    stdin = open('./input.txt', 'r')
    num_of_traffic_lights, k, broken_traffic_lights = map(int, stdin.readline().split())

    traffic_lights = [1] * (num_of_traffic_lights + 1)
    for _ in range(broken_traffic_lights):
        traffic_lights[int(stdin.readline())] = 0

    broken_lights_prefix = [0] * (num_of_traffic_lights + 1)
    count = 0
    for idx in range(1, k + 1):
        if traffic_lights[idx] == 0:
            count += 1
    broken_lights_prefix[k] = count

    for idx in range(k + 1, len(traffic_lights)):
        count = broken_lights_prefix[idx - 1]
        if traffic_lights[idx] == 0:
            count += 1
        if traffic_lights[idx - k] == 0:
            count -= 1
        broken_lights_prefix[idx] = count

    print(min(broken_lights_prefix[k:]))


if __name__ == '__main__':
    main()
