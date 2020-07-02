from sys import stdin

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

def main():
    x, y = map(int, stdin.readline().split())

    print(x + y - gcd(x, y))

if __name__ == '__main__':
    main()
