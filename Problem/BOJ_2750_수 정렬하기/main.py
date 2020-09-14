from sys import stdin

def main():
    N = int(stdin.readline().rstrip())
    numbers = []

    for _ in range(N):
        numbers.append(int(stdin.readline().rstrip()))

    numbers.sort()

    for number in numbers:
        print(number)

if __name__ == '__main__':
    main()