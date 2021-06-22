from sys import stdin


class Main:
    def __init__(self):
        self.rectangles = []

        self.main()

    def union_area(self):
        ys = set()
        events = []
        answer = 0

        for idx, rec in enumerate(self.rectangles):
            ys.add(rec["y1"])
            ys.add(rec["y2"])
            events.append([rec["x1"], (1, idx)])
            events.append([rec["x2"], (-1, idx)])

        ys = sorted(list(ys))
        events.sort()

        dup_count = [0] * (len(ys) - 1)

        for i, event in enumerate(events):
            x, (delta, rec) = event
            y1 = self.rectangles[rec]["y1"]
            y2 = self.rectangles[rec]["y2"]

            for j, y in enumerate(ys):
                if y1 <= y < y2:
                    dup_count[j] += delta

            cut_length = 0
            for j, dup in enumerate(dup_count):
                if dup > 0:
                    cut_length += ys[j + 1] - ys[j]

            if i + 1 < len(events):
                answer += cut_length * (events[i + 1][0] - events[i][0])

        return answer

    def main(self):
        stdin = open("./input.txt", "r")
        num_of_recs = int(stdin.readline())

        for _ in range(num_of_recs):
            vertical, horizontal = map(int, stdin.readline().split())
            self.rectangles.append(
                {"x1": vertical, "x2": vertical + 10, "y1": horizontal, "y2": horizontal + 10}
            )

        print(self.union_area())


if __name__ == '__main__':
    Main()