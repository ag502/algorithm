from sys import stdin


def can_install(distance):
    cur_home_pos = house_pos[0]
    count = 1
    for idx in range(1, len(house_pos)):
        if house_pos[idx] - cur_home_pos >= distance:
            cur_home_pos = house_pos[idx]
            count += 1
    if count >= num_of_routers:
        return True
    return False


def binary_search():
    start = 0
    end = max(house_pos)

    while start <= end:
        mid = (start + end) // 2
        if can_install(mid):
            start = mid + 1
        else:
            end = mid - 1
    return end


def main():
    stdin = open("./input.txt", "r")
    global num_of_homes, num_of_routers, house_pos

    num_of_homes, num_of_routers = map(int, stdin.readline().split())
    house_pos = []
    for _ in range(num_of_homes):
        house_pos.append(int(stdin.readline()))
    house_pos.sort()

    print(binary_search())


if __name__ == '__main__':
    main()