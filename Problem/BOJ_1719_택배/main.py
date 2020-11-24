from sys import stdin

def main():
    stdin = open('./input.txt', 'r')
    num_of_stock_places, num_of_paths = map(int, stdin.readline().split())

    stock_places = [[float('inf')] * (num_of_stock_places + 1) for _ in range(num_of_stock_places + 1)]
    for i in range(num_of_stock_places + 1):
        stock_places[i][i] = 0

    for _ in range(num_of_paths):
        start, finish, time = map(int, stdin.readline().split())
        stock_places[start][finish] = time
        stock_places[finish][start] = time

    stop_places = [[0] * (num_of_stock_places + 1) for _ in range(num_of_stock_places + 1)]

    for k in range(1, num_of_stock_places + 1):
        for i in range(1, num_of_stock_places + 1):
            if stock_places[i][k] == float('inf'):
                continue
            for j in range(1, num_of_stock_places + 1):
                if stock_places[i][k] + stock_places[k][j] < stock_places[i][j]:
                    stock_places[i][j] = stock_places[i][k] + stock_places[k][j]
                    if stop_places[i][j] == 0:
                        stop_places[i][j] = k
                #     print('1 ' + str(k))
                elif stock_places[i][k] + stock_places[k][j] > stock_places[i][j]:
                    if stop_places[i][j] == 0:
                        stop_places[i][j] = j
                    # print('2 ' + str(j))
    print(stock_places)
    print(stop_places)


if __name__ == '__main__':
    main()