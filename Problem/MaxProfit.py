def max_profit_memo(price_list, count, cache):
    if count < 2:
        return price_list[count]
    if count in cache:
        return cache[count]
    max_cost = price_list[count] if count < len(price_list) else - 1
    for i in range(1, count // 2 + 1):
        value = max_profit_memo(price_list, count - i, cache) + max_profit_memo(price_list, i, cache)
        if max_cost < value:
            max_cost = value
    cache[count] = max_cost
    return cache[count]


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
