from sys import stdin


def main():
    test_case = int(stdin.readline().rstrip())

    for _ in range(test_case):
        x, y = map(int, stdin.readline().split())

        distance = y - x

        if distance == 1:
            print(1)
        elif distance == 2:
            print(2)
        else:
            start = 3
            interval = 2
            count = 0
            while start <= distance:
                if count != 0 and count % 2 == 0:
                    interval += 1
                start += interval
                count += 1

            print(interval + (start - interval) // interval)


if __name__ == "__main__":
    main()
