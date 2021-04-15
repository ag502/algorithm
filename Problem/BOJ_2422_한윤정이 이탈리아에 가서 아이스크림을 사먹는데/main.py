from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    answer = 0
    num_of_ice_cream, num_of_bad = map(int, stdin.readline().split())

    check = [[True] * (num_of_ice_cream + 1) for _ in range(num_of_ice_cream + 1)]

    for _ in range(num_of_bad):
        ice_cream_1, ice_cream_2 = map(int, stdin.readline().split())
        check[ice_cream_1][ice_cream_2] = False
        check[ice_cream_2][ice_cream_1] = False

    for i in range(1, num_of_ice_cream + 1):
        for j in range(i + 1, num_of_ice_cream + 1):
            if check[i][j]:
                for k in range(j + 1, num_of_ice_cream + 1):
                    if check[i][k] and check[j][k]:
                        answer += 1

    print(answer)


if __name__ == '__main__':
    main()