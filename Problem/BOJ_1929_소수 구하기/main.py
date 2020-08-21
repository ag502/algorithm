from sys import stdin


def main():
    prime = [i for i in range(1000001)]

    for i in range(2, int(1000000 ** 0.5) + 1):
        for j in range(i * i, 1000000 + 1, i):
            prime[j] = 0
    prime[1] = 0
    M, N = map(int, stdin.readline().split())
    for index in range(M, N + 1):
        if prime[index] != 0:
            print(prime[index])


if __name__ == "__main__":
    main()
