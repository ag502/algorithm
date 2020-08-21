from sys import stdin


def main():
    prime = [i for i in range(10001)]
    for i in range(2, int(10000 ** 0.5) + 1):
        for j in range(i * i, 10001, i):
            prime[j] = 0
    prime[1] = 0

    M = int(stdin.readline().rstrip())
    N = int(stdin.readline().rstrip())
    selected_prime = []

    for index in range(M, N + 1):
        if prime[index] != 0:
            selected_prime.append(prime[index])

    if not selected_prime:
        print(-1)
    else:
        print(sum(selected_prime))
        print(selected_prime[0])


if __name__ == "__main__":
    main()
