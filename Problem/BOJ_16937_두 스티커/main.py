from sys import stdin
from typing import List, Tuple


def input() -> Tuple[int, int, int, List[List[int]]]:
    stdin = open("./input.txt", "r")

    height: int
    width: int
    height, width = list(map(int, stdin.readline().split()))

    num_of_sticker: int
    num_of_sticker = int(stdin.readline())

    stickers: List[List[int]] = []

    sticker_1: int
    sticker_2: int
    for sticker in range(num_of_sticker):
        sticker_1, sticker_2 = list(map(int, stdin.readline().split()))

        stickers.append([sticker_1, sticker_2, sticker])
        if sticker_1 != sticker_2:
            stickers.append([sticker_2, sticker_1, sticker])

    return height, width, num_of_sticker, stickers

sum_of_area = 0


def main() -> None:
    global sum_of_area

    height, width, num_of_sticker, stickers = input()

    visited: List[bool] = [False] * len(stickers)
    selected_sticker: List[bool] = [False] * num_of_sticker

    def select_sticker(cur_sticker: int, sticker: List[List[int]] = []):
        global sum_of_area

        cur_sticker_num = stickers[cur_sticker][2]
        sticker.append(stickers[cur_sticker])
        visited[cur_sticker] = True
        selected_sticker[cur_sticker_num] = True

        if len(sticker) < 2:
            for next_sticker in range(cur_sticker, len(stickers)):
                if not visited[next_sticker] and not selected_sticker[stickers[next_sticker][2]]:
                    select_sticker(next_sticker, sticker)
        elif len(sticker) == 2:
            height_1, width_1 = [sticker[0][0], sticker[0][1]]
            height_2, width_2 = [sticker[1][0], sticker[1][1]]

            if height_1 <= height and height_2 <= height and width_1 <= width and width_2 <= width:
                if height_1 + height_2 <= height:
                    sum_of_area = max(sum_of_area, height_1 * width_1 + height_2 * width_2)

                elif width_1 + width_2 <= width:
                    sum_of_area = max(sum_of_area, height_1 * width_1 + height_2 * width_2)

        sticker.pop()
        visited[cur_sticker] = False
        selected_sticker[stickers[cur_sticker][2]] = False

    for start_sticker in range(len(stickers)):
        select_sticker(start_sticker)

    print(sum_of_area)


if __name__ == '__main__':
    main()