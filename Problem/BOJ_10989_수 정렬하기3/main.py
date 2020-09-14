from sys import stdin


def main():
    N = int(stdin.readline().rstrip())
    numbers = [0] * 10001

    for _ in range(N):
        numbers[int(stdin.readline().rstrip())] += 1

    for number in range(1, 10001):
        for _ in range(numbers[number]):
            print(number)

if __name__ == "__main__":
    main()