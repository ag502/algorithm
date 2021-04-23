from sys import stdin


def get_sum(money_list, standard):
    money_sum = 0
    for money in money_list:
        if money > standard:
            money_sum += standard
        else:
            money_sum += money
    return money_sum


def main():
    stdin = open("./input.txt", "r")
    num_of_province = int(stdin.readline())
    province_money = list(map(int, stdin.readline().split()))
    maximum_money = int(stdin.readline())

    start = 0
    end = max(province_money)

    while start <= end:
        mid = (start + end) // 2
        money_sum = get_sum(province_money, mid)

        if money_sum > maximum_money:
            end = mid - 1
        else:
            start = mid + 1
    print(end)


if __name__ == '__main__':
    main()