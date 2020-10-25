from sys import stdin

def main():
    stdin = open('./test_case.txt', 'r')
    m = int(stdin.readline())
    numbers = list(map(float, stdin.readline().split()))

    ranges = [0] * m
    l = 1 / m
    for number in numbers:
        idx = round(number / l, 10)
        ranges[int(idx)] += 1

    print(' '.join(map(str, ranges)))

if __name__ == '__main__':
    main()