from sys import stdin
from re import compile


def main():
    stdin = open('./input.txt', 'r')
    test_case = int(stdin.readline())
    regex = compile('(100+1+|01)+')

    for _ in range(test_case):
        signal = stdin.readline().strip()
        print(regex.fullmatch(signal))
        if regex.fullmatch(signal) is None:
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    main()