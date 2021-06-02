from sys import stdin, maxsize
from collections import deque


class Main:
    def __init__(self):
        self.city_length = 0
        self.max_count = 0
        self.city = []

        self.selected_chicken_stores = deque()
        self.houses = deque()
        self.chicken_stores = deque()
        self.min_chicken_distance = maxsize

        self.main()

    def calc_distance(self, chicken_stores):
        cur_chicken_distance = 0
        for house_position in self.houses:
            temp_distance = maxsize
            for chicken_position in chicken_stores:
                temp_distance = min(temp_distance, abs(house_position[0] - chicken_position[0]) + abs(house_position[1] - chicken_position[1]))
            cur_chicken_distance += temp_distance

        return cur_chicken_distance

    def select_closed_chicken_store(self, cur_store, count, cur_stores=deque()):
        cur_stores.append(self.chicken_stores[cur_store])

        if len(cur_stores) < count:
            for next_store in range(cur_store + 1, len(self.chicken_stores)):
                self.select_closed_chicken_store(next_store, count, cur_stores)
        elif len(cur_stores) == count:
            self.selected_chicken_stores.append(cur_stores.copy())
        cur_stores.pop()

    def main(self):
        stdin = open("./input.txt", "r")
        self.city_length, self.max_count = map(int, stdin.readline().split())

        for _ in range(self.city_length):
            self.city.append(list(map(int, stdin.readline().split())))

        for i in range(self.city_length):
            for j in range(self.city_length):
                if self.city[i][j] == 1:
                    self.houses.append((i, j))
                elif self.city[i][j] == 2:
                    self.chicken_stores.append((i, j))

        for start_chicken_store in range(len(self.chicken_stores)):
            for count in range(1, self.max_count + 1):
                self.select_closed_chicken_store(start_chicken_store, count)

        for chicken_stores in self.selected_chicken_stores:
            self.min_chicken_distance = min(self.min_chicken_distance, self.calc_distance(chicken_stores))

        print(self.min_chicken_distance)


if __name__ == '__main__':
    Main()