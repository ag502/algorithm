from sys import stdin, maxsize


def can_install(street_lamp_positions, length_of_bridge, height):
    cur_light = 0
    for street_lamp_position in street_lamp_positions:
        if street_lamp_position - height <= cur_light:
            cur_light += street_lamp_position + height
        else:
            return False
    if cur_light < length_of_bridge:
        return False
    return True


def binary_search(street_lamp_positions, length_of_bridge):
    start_height = 0
    end_height = maxsize

    while start_height <= end_height:
        mid_height = (start_height + end_height) // 2

        if can_install(street_lamp_positions, length_of_bridge, mid_height):
            end_height = mid_height - 1
        else:
            start_height = mid_height + 1
    return start_height


def main():
    stdin = open('./input.txt', 'r')
    length_of_bridge = int(stdin.readline())
    num_of_street_lamp = int(stdin.readline())
    street_lamp_positions = list(map(int, stdin.readline().split()))

    print(binary_search(street_lamp_positions, length_of_bridge))


if __name__ == '__main__':
    main()