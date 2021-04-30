from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    num_of_train, num_of_order = map(int, stdin.readline().split())

    trains = [[0] * 21 for _ in range(num_of_train + 1)]

    for _ in range(num_of_order):
        order_info = list(map(int, stdin.readline().split()))
        order = order_info[0]

        if order == 1 or order == 2:
            train_number, seat_number = order_info[1:]
            if order == 1:
                if trains[train_number][seat_number] == 0:
                    trains[train_number][seat_number] = 1
            else:
                if trains[train_number][seat_number] == 1:
                    trains[train_number][seat_number] = 0
        elif order == 3 or order == 4:
            train_number = order_info[1]
            if order == 3:
                for idx in range(20, 0, -1):
                    if trains[train_number][idx] == 1:
                        if idx == 20:
                            trains[train_number][idx] = 0
                        else:
                            trains[train_number][idx] = 0
                            trains[train_number][idx + 1] = 1
            else:
                for idx in range(1, 21):
                    if trains[train_number][idx] == 1:
                        if idx == 1:
                            trains[train_number][idx] = 0
                        else:
                            trains[train_number][idx] = 0
                            trains[train_number][idx - 1] = 1

    can_pass = set()
    answer = 0
    for train in trains[1:]:
        cur_train = ''.join(map(str, train))
        # print(cur_train)
        if cur_train in can_pass:
            continue
        else:
            can_pass.add(cur_train)
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()