from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    n, k = map(int, stdin.readline().split())

    answer = 0
    for hour in range(n + 1):
        for minute in range(60):
            for second in range(60):
                time = ""
                if hour <= 9:
                    time += "0" + str(hour)
                else:
                    time += str(hour)

                if minute <= 9:
                    time += "0" + str(minute)
                else:
                    time += str(minute)

                if second <= 9:
                    time += "0" + str(second)
                else:
                    time += str(second)

                if str(k) in time:
                    answer += 1

    print(answer)


if __name__ == '__main__':
    main()