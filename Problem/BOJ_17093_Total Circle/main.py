from sys import stdin


class Main:
    def __init__(self):
        self.p_cor = []
        self.q_cor = []

        self.main()

    def cal_dist(self, cent_x, cent_y, target_x, target_y):
        return (cent_x - target_x) ** 2 + (cent_y - target_y) ** 2

    def main(self):
        stdin = open("./input.txt", "r")
        n, m = map(int, stdin.readline().split())

        for _ in range(n):
            self.p_cor.append(tuple(map(int, stdin.readline().split())))

        for _ in range(m):
            self.q_cor.append(tuple(map(int, stdin.readline().split())))

        max_dist = 0
        for q_cor_x, q_cor_y in self.q_cor:
            for p_cor_x, p_cor_y in self.p_cor:
                max_dist = max(max_dist, self.cal_dist(q_cor_x, q_cor_y, p_cor_x, p_cor_y))

        print(max_dist)


if __name__ == '__main__':
    Main()