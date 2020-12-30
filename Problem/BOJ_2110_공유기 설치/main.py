from sys import stdin


def can_install(houses, distance, num_of_routers):
    cur_house = houses[0]
    count = 1
    for idx in range(1, len(houses)):
        if houses[idx] - cur_house >= distance:
            cur_house = houses[idx]
            count += 1
    return num_of_routers <= count


def main():
    stdin = open('./input.txt', 'r')
    num_of_houses, num_of_routers = map(int, stdin.readline().split())
    houses = [0] * num_of_houses

    for idx in range(num_of_houses):
        houses[idx] = int(stdin.readline())

    houses.sort()

    start = 1
    end = max(houses)
    answer = -1
    while start <= end:
        mid = (start + end) // 2
        if can_install(houses, mid, num_of_routers):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)


if __name__ == '__main__':
    main()