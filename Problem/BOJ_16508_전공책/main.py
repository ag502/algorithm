from sys import stdin, maxsize


class Main:
    def __init__(self):
        self.target_string = ''
        self.target_string_dict = {}
        self.num_of_book = 0
        self.string = []
        self.price = []
        self.using_book = {}
        self.visited = []
        self.total_price = maxsize

        self.main()

    def find_char(self, cur_idx, word=[]):
        cur_char_info = self.string[cur_idx]
        word.append(cur_char_info[2])
        self.using_book[cur_char_info[1]] += 1
        self.visited[cur_idx] = True

        if len(word) < len(self.target_string):
            for next_idx in range(len(self.string)):
                next_char_info = self.string[next_idx]
                if not self.visited[next_idx] and next_char_info[2] == self.target_string[len(word)]:
                    self.find_char(next_idx, word)
        elif len(word) == len(self.target_string):
            # print(word)
            # print(self.using_book)
            temp = 0
            for book, count in self.using_book.items():
                if count != 0:
                    temp += self.price[book]

            if temp != 0:
                self.total_price = min(self.total_price, temp)

        word.pop()
        self.using_book[cur_char_info[1]] -= 1
        self.visited[cur_idx] = False

    def main(self):
        stdin = open("./input.txt", "r")
        self.target_string = stdin.readline().rstrip()

        for idx, char in enumerate(self.target_string):
            self.target_string_dict[char] = idx

        self.num_of_book = int(stdin.readline())

        for idx in range(self.num_of_book):
            price, title = stdin.readline().split()
            self.using_book[idx] = 0
            self.price.append(int(price))
            for title_char in title:
                if title_char in self.target_string:
                    self.string.append([int(price), idx, title_char])

        self.visited = [False] * len(self.string)
        self.string.sort(key=lambda x: x[1])

        for idx, char_info in enumerate(self.string):
            if self.target_string[0] == char_info[2]:
                self.find_char(idx)
            else:
                break

        print(-1 if self.total_price == maxsize else self.total_price)


if __name__ == '__main__':
    Main()
