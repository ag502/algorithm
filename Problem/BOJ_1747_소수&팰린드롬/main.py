from sys import stdin

def sieve():
    numbers = [i for i in range(0, 1004001)]
    for i in range(2, int(1004000 ** 0.5) + 1):
        for j in range(i * i, 1004001, i):
            if numbers[j] == j:
                numbers[j] = -1
    numbers[0] = -1
    numbers[1] = -1
    return numbers

def main():
    stdin = open('./test_case.txt', 'r')
    n = int(stdin.readline())
    primes = sieve()

    for i in range(n, len(primes)):
        if primes[i] != -1:
            string_num = list(str(primes[i]))
            reverse_string_num = reversed(string_num)
            if primes[i] == int(''.join(reverse_string_num)):
                print(primes[i])
                break

if __name__ == '__main__':
    main()