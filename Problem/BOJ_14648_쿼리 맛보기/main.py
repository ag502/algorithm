from sys import stdin


class Main:
    def __init__(self):
        self.sequence = None

        self.main()

    def main(self):
        stdin = open("input.txt", "r")
        len_of_sequence, num_of_queries = map(int, stdin.readline().split())

        self.sequence = list(map(int, stdin.readline().split()))
        for _ in range(num_of_queries):
            type, *seq_range = map(int, stdin.readline().split())

            if type == 1:
                a, b = seq_range
                print(sum(self.sequence[a - 1:b]))
                [self.sequence[a - 1], self.sequence[b - 1]] = [self.sequence[b - 1], self.sequence[a - 1]]
            elif type == 2:
                a, b, c, d = seq_range
                print(sum(self.sequence[a - 1:b]) - sum(self.sequence[c - 1:d]))


if __name__ == '__main__':
    Main()