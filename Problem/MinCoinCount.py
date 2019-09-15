def min_coin_count(value, coin_list):
    coin_list.sort(reverse=True)
    # index = 0
    num_coin = 0
    # while value > 0:
    #     if value >= coin_list[index]:
    #         value -= coin_list[index]
    #         num_coin += 1
    #     else:
    #         index += 1
    # return num_coin
    for coin in coin_list:
        num_coin += value // coin
        value = value % coin
    return num_coin


default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))
