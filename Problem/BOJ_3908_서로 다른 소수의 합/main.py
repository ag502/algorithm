from sys import stdin
from itertools import combinations


def get_prime_list(number):
    number_list = [i for i in range(number + 1)]
    prime_list = []

    for i in range(2, int(number ** 0.5) + 1):
        for j in range(2, number // i + 1):
            if number_list[i * j] != -1:
                number_list[i * j] = -1

    for i in range(2, len(number_list)):
        if number_list[i] != -1:
            prime_list.append(number_list[i])

    return prime_list


def main():
    num_of_test_case = int(stdin.readline())

    for _ in range(num_of_test_case):
        number, num_of_prime = map(int, stdin.readline().split())
        answer = 0

        print(get_prime_list(number))

        # prime_comb = list(combinations(get_prime_list(number), num_of_prime))

        # for comb in prime_comb:
        #     if sum(comb) == number:
        #         answer += 1

        print(answer)


if __name__ == "__main__":
    main()
