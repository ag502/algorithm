from sys import stdin


class Main:
    def __init__(self):
        stdin = open("./input.txt", "r")
        self.num_of_bottle, self.num_of_people = map(int, stdin.readline().split())
        self.alcohols = [int(stdin.readline()) for _ in range(self.num_of_bottle)]
        self.alcohols.sort()

        self.main()

    def share_alcohol(self, ml):
        total_people = 0
        for alcohol in self.alcohols:
            total_people += alcohol // ml

        return total_people

    def upper_bound(self, target):
        start_ml = 0
        finish_ml = max(self.alcohols) + 1

        while start_ml < finish_ml:
            mid_ml = (start_ml + finish_ml) // 2
            total_people = self.share_alcohol(mid_ml)

            if total_people >= target:
                start_ml = mid_ml + 1
            else:
                finish_ml = mid_ml

        return finish_ml - 1

    def main(self):
        answer = self.upper_bound(self.num_of_people)
        print(answer)


if __name__ == '__main__':
    Main()