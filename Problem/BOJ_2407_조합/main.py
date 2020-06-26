from sys import stdin

def combination(n, r):
    if r == 1:
        return n
    if n == r:
        return 1

    smallest_r = min(r, n - r)
    denominator = 1
    numerator = 1

    for i in range(0, smallest_r):
        denominator *= (n - i)
    for i in range(1, smallest_r + 1):
        numerator *= i

    return denominator // numerator

def main():
    n, r = map(int, stdin.readline().split())
    print(combination(n, r))

if __name__ == '__main__':
    main()