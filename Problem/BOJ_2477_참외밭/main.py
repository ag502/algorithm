from sys import stdin

def main():
    stdin = open('./test_case.txt', 'r')
    fruit_per_area = int(stdin.readline())
    # 한 변의 정보
    side_info = {}
    # 변의 순서
    sides = []

    for _ in range(6):
        direction, length = map(int, stdin.readline().split())
        if direction not in side_info:
            side_info[direction] = []
        side_info[direction].append(length)
        sides.append(length)

    # 최대 가로 길이, 최대 세로 길이
    max_width = max_height = 0
    for direction, length in side_info.items():
        if len(length) == 1:
            if direction == 3 or direction == 4:
                max_height = length[0]
            elif direction == 1 or direction == 2:
                max_width = length[0]
    # 비어있는 사각형의 변 찾기
    empty_width = 0
    empty_height = 0
    print(sides)
    for idx in range(len(sides)):
        # 정사각형 제외
        if empty_width == 0 and sides[idx - 1] + sides[(idx + 1) % 6] == max_height:
            empty_width = sides[idx]
        elif sides[idx - 1] + sides[(idx + 1) % 6] == max_width:
            empty_height = sides[idx]

    print(fruit_per_area * (max_width * max_height - empty_width * empty_height))

if __name__ == '__main__':
    main()
