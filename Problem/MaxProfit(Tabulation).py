def max_profit(price_list, count):
    max_costs = [0, price_list[1]]
    for i in range(2, count + 1):
        max_cost = price_list[i] if i < len(price_list) else - 1
        for j in range(1, i // 2 + 1):
            max_cost = max(max_cost, max_costs[i - j] + max_costs[j])
        max_costs.append(max_cost)
    return max_costs[count]


print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
