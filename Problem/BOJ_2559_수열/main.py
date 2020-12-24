from sys import stdin

MAX = 100001

def main():
    stdin = open('./input.txt', 'r')
    total_days, standard_days = map(int, stdin.readline().split())
    temperature = list(map(int, stdin.readline().split()))

    dp = [-987654321] * MAX
    sum_of_temperature = 0
    for day in range(standard_days):
        sum_of_temperature += temperature[day]
    dp[0] = sum_of_temperature

    for day in range(1, total_days - (standard_days - 1)):
        dp[day] = dp[day - 1] - temperature[day - 1] + temperature[day + (standard_days - 1)]

    print(max(dp))

if __name__ == '__main__':
    main()