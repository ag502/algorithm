from sys import stdin


class Main:
    def __init__(self):
        self.coors = []

        self.main()

    def union_line(self):
        xs = set()

        for x1, x2 in self.coors:
            xs.add(x1)
            xs.add(x2)

        xs = sorted(list(xs))
        count = [0] * (len(xs) - 1)

        for i, (x1, x2) in enumerate(self.coors):
            for j, x in enumerate(xs):
                if x1 <= x < x2:
                    count[j] += 1

        return max(count)

    def main(self):
        stdin = open("./input.txt", "r")
        num_of_lines = int(stdin.readline())

        for _ in range(num_of_lines):
            self.coors.append(tuple(map(int, stdin.readline().split())))

        print(self.union_line())


if __name__ == '__main__':
    Main()