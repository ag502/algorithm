from sys import stdin


def main():
    num_of_factors = [0] * (int(1e7) + 1)

    for i in range(1, len(num_of_factors)):
        for j in range(i, len(num_of_factors), i):
            num_of_factors[j] += 1

    C = int(stdin.readline())
    for _ in range(C):
        L, U = map(int, stdin.readline().split())
        answer = 0
        for i in range(L, U + 1):
            if answer < num_of_factors[i]:
                answer = num_of_factors[i]
        print(answer)


if __name__ == "__main__":
    main()
