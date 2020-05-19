from sys import stdin

def gcd(n, m):
    if n % m == 0:
        return m
    return gcd(m, n % m)

def main():
    n, m = map(int, stdin.readline().split())
    print(m - gcd(n, m))


if __name__ == "__main__":
    main()