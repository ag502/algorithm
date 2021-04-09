from sys import stdin, maxsize

stdin = open("./input.txt", "r")
num_of_snowball = int(stdin.readline())
snowballs = list(map(int, stdin.readline().split()))


def main():
    snowballs.sort()

    answer = maxsize
    for i in range(num_of_snowball - 1):
        for j in range(i + 1, num_of_snowball):
            snow_man_1 = snowballs[i] + snowballs[j]
            start = 0
            end = num_of_snowball - 1
            while start < end:
                if start == i or start == j:
                    start += 1
                    continue
                if end == i or end == j:
                    end -= 1
                    continue

                snow_man_2 = snowballs[start] + snowballs[end]
                answer = min(answer, abs(snow_man_1 - snow_man_2))
                if snow_man_2 < snow_man_1:
                    start += 1
                elif snow_man_2 > snow_man_1:
                    end -= 1
                else:
                    start += 1
                    end -= 1
                    print(answer)
                    return

    print(answer)


if __name__ == '__main__':
    main()