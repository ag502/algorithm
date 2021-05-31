from sys import stdin


class Main:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.num_of_stickers = 0
        self.stickers = []
        self.visited = None
        self.selected_sticker = None
        self.max_area = 0

        self.main()

    def main(self):
        stdin = open("./input.txt", "r")
        self.height, self.width = map(int, stdin.readline().split())
        self.num_of_stickers = int(stdin.readline())

        for sticker in range(self.num_of_stickers):
            sticker_1, sticker_2 = map(int, stdin.readline().split())
            self.stickers.append([sticker_1, sticker_2, sticker])

            if sticker_1 != sticker_2:
                self.stickers.append([sticker_2, sticker_1, sticker])

        self.visited = [False] * len(self.stickers)
        self.selected_sticker = [False] * self.num_of_stickers

        for start_sticker in range(len(self.stickers)):
            self.pick_sticker(start_sticker)

        print(self.max_area)

    def pick_sticker(self, cur_sticker, two_stickers=[]):
        cur_sticker_h, cur_sticker_w, cur_sticker_no = self.stickers[cur_sticker]
        two_stickers.append(self.stickers[cur_sticker])
        self.visited[cur_sticker] = True
        self.selected_sticker[cur_sticker_no] = True

        if len(two_stickers) < 2:
            for next_sticker in range(cur_sticker + 1, len(self.stickers)):
                next_sticker_h, next_sticker_w, next_sticker_no = self.stickers[next_sticker]
                if not self.visited[next_sticker] and not self.selected_sticker[next_sticker_no]:
                    self.pick_sticker(next_sticker, two_stickers)
        elif len(two_stickers) == 2:
            self.check_attach(two_stickers[0], two_stickers[1])
        two_stickers.pop()
        self.visited[cur_sticker] = False
        self.selected_sticker[cur_sticker_no] = False

    def check_attach(self, sticker_1, sticker_2):
        height_1, width_1, _ = sticker_1
        height_2, width_2, _ = sticker_2

        if height_1 <= self.height and height_2 <= self.height and \
                width_1 <= self.width and width_2 <= self.width:
            if height_1 + height_2 <= self.height or width_1 + width_2 <= self.width:
                self.max_area = max(self.max_area, height_1 * width_1 + height_2 * width_2)


if __name__ == '__main__':
    Main()
