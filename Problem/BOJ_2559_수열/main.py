from sys import stdin

def main():
    stdin = open('./input.txt', 'r')
    total_days, standard_days = map(int, stdin.readline().split())
    temperature = list(map(int, stdin.readline().split()))

    sum_of_sub_temperature = []
    for i in range(len(temperature) - standard_days + 1):
        temp = 0
        for j in range(standard_days):
            temp += temperature[i + j]
        sum_of_sub_temperature.append(temp)

    print(max(sum_of_sub_temperature))

if __name__ == '__main__':
    main()