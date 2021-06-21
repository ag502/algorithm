from sys import stdin


class Main:
    def __init__(self):
        self.rectangles = []
        self.ret = 0

        self.main()

    def union_area(self):
        if not self.rectangles:
            return
        events = []
        ys = set()

        for idx, rectangle in enumerate(self.rectangles):
            ys.add(rectangle["y1"])
            ys.add(rectangle["y2"])
            events.append((rectangle["x1"], (1, idx)))
            events.append((rectangle["x2"], (-1, idx)))

        ys = sorted(list(ys))
        events.sort()

        count = [0] * (len(ys) - 1)

        for idx, event in enumerate(events):
            x, (delta, rec) = event
            y1 = self.rectangles[rec]["y1"]
            y2 = self.rectangles[rec]["y2"]
            for i in range(len(ys)):
                if y1 <= ys[i] < y2:
                    count[i] += delta

            cut_length = 0
            for i in range(len(count)):
                if count[i] > 0:
                    cut_length += ys[i + 1] - ys[i]

            if idx + 1 < len(events):
                self.ret += cut_length * ((events[idx + 1])[0] - x)

    def main(self):
        stdin = open("./input.txt", "r")
        num_of_paper = int(stdin.readline())
        for _ in range(num_of_paper):
            vertical, cross = map(int, stdin.readline().split())
            self.rectangles.append(({"x1": vertical, "x2": 10 + vertical, "y1": cross, "y2": 10 + cross}))

        self.union_area()
        print(self.ret)


if __name__ == '__main__':
    Main()
