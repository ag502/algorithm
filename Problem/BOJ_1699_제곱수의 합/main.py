from sys import stdin


def main():
    N = int(stdin.readline())
    sum_of_power = [0] * (N + 1)

    for i in range(2, int(N ** 0.5) + 1):
        power = i ** 2
        for j in range(1, (N // power) + 1):
            if sum_of_power[power * j] == 0:
                sum_of_power[power * j] = j
            else:
                sum_of_power[power * j] = min(sum_of_power[power * j], j)

    sum_of_power[1] = 1
    for index in range(2, N + 1):
        if sum_of_power[index] == 0:
            sum_of_power[index] = sum_of_power[index - 1] + 1
        else:
            continue
    print(sum_of_power)


if __name__ == "__main__":
    main()
