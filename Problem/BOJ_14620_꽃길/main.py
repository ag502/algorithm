from sys import stdin, maxsize

moving_dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]


class Main:
    def __init__(self):
        self.land_length = 0
        self.land = []
        self.visited = None
        self.min_cost = maxsize

        self.main()

    def plant_flower(self, cur_row, cur_col, cur_cost, cur_planted_flower):
        # 씨앗 놓이는 위치 방문 체크
        self.visited[cur_row][cur_col] = True
        # 꽃 잎의 위치들 방문 체크
        for moving_row, moving_col in moving_dir:
            next_row = cur_row + moving_row
            next_col = cur_col + moving_col
            if 0 <= next_row < self.land_length and 0 <= next_col < self.land_length:
                self.visited[next_row][next_col] = True
                cur_cost += self.land[next_row][next_col]

        cur_cost += self.land[cur_row][cur_col]

        if cur_planted_flower < 3:
            for next_row in range(1, self.land_length - 1):
                for next_col in range(1, self.land_length - 1):
                    # 씨앗 놓는 곳
                    if not self.visited[next_row][next_col]:
                        # 꽃 잎들의 위치
                        for moving_row, moving_col in moving_dir:
                            # 꽃 잎들이 다른 꽃 잎과 겹치는지 확인
                            if self.visited[next_row + moving_row][next_col + moving_col]:
                                break
                        else:
                            self.plant_flower(next_row, next_col, cur_cost, cur_planted_flower + 1)
        elif cur_planted_flower == 3:
            self.min_cost = min(self.min_cost, cur_cost)

        self.visited[cur_row][cur_col] = False
        for moving_row, moving_col in moving_dir:
            next_row = cur_row + moving_row
            next_col = cur_col + moving_col
            if 0 <= next_row < self.land_length and 0 <= next_col < self.land_length:
                self.visited[next_row][next_col] = False

    def main(self):
        stdin = open("./input.txt", "r")
        self.land_length = int(stdin.readline())

        for _ in range(self.land_length):
            self.land.append(list(map(int, stdin.readline().split())))

        self.visited = [[False] * self.land_length for _ in range(self.land_length)]

        for start_row in range(1, self.land_length - 1):
            for start_col in range(1, self.land_length - 1):
                self.plant_flower(start_row, start_col, 0, 1)

        print(self.min_cost)


if __name__ == '__main__':
    Main()