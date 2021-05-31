from sys import stdin, maxsize


class Main:
    def __init__(self):
        self.target_string = None
        self.num_of_book = 0
        self.all_title = []
        self.visited = []
        self.books = []
        self.min_cost = maxsize

        self.main()

    def get_book_comb(self, cur_idx, count, target_number, acc_cost, acc_title=[]) -> None:
        cur_price, cur_title = self.books[cur_idx]
        self.visited[cur_idx] = True
        acc_cost += cur_price
        acc_title.append(cur_title)

        if count < target_number:
            for next_idx in range(cur_idx + 1, self.num_of_book):
                if not self.visited[next_idx]:
                    self.get_book_comb(next_idx, count + 1, target_number, acc_cost, acc_title)
        elif count == target_number:
            self.all_title.append([acc_cost, ''.join(acc_title)])
        self.visited[cur_idx] = False
        acc_title.pop()

    def check_word(self):
        for cost, book_title in self.all_title:
            book_title = list(book_title)
            for char in self.target_string:
                try:
                    idx = book_title.index(char)
                    book_title[idx] = "_"
                except:
                    break

            else:
                self.min_cost = min(self.min_cost, cost)

    def main(self) -> None:
        stdin = open("./input.txt", "r")
        self.target_string = stdin.readline().rstrip()
        self.num_of_book = int(stdin.readline())

        for _ in range(self.num_of_book):
            price, title = stdin.readline().split()
            self.books.append([int(price), title])

        self.visited = [False] * self.num_of_book

        for count in range(1, self.num_of_book + 1):
            for book in range(self.num_of_book):
                self.get_book_comb(book, 1, count, 0)

        self.check_word()
        print(-1 if self.min_cost == maxsize else self.min_cost)


if __name__ == '__main__':
    Main()