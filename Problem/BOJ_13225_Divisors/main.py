from sys import stdin


def main():
    min_factors = [i for i in range(10000)]
    min_factor_powers = [0] * (10000)
    factors = [0] * (10000)

    for i in range(2, int(10000) + 1):
        for j in range(i * i, len(min_factors), i):
            if min_factors[j] == j:
                min_factors[j] = i

    min_factor_powers[1] = 1
    factors[1] = 1
    for i in range(2, len(min_factor_powers)):
        if min_factors[i] == i:
            min_factor_powers[i] = 1
            factors[i] = 2
        else:
            p = min_factors[i]
            if p != min_factors[i // p]:
                min_factor_powers[i] = 1
            else:
                min_factor_powers[i] = min_factor_powers[i // p] + 1
            factors[i] = int((factors[i // p] / min_factor_powers[i]
                              ) * (min_factor_powers[i] + 1))

    C = int(stdin.readline())
    for _ in range(C):
        N = int(stdin.readline())
        print(str(N) + " " + str(factors[N]))


if __name__ == "__main__":
    main()
