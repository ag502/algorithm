from sys import stdin
from itertools import combinations_with_replacement as cr


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
    num_of_testcase = int(stdin.readline())

    for _ in range(num_of_testcase):
        number = int(stdin.readline())
        prime_list = get_prime_list(number)
        prime_comb = list(cr(prime_list, 2))

        for comb in prime_comb:

            if number - sum(comb) in prime_list:
                third_number = number - sum(comb)
                answer = ''
                for num in comb:
                    answer += str(num) + ' '
                print(answer.rstrip() + ' ' + str(third_number))
                break
        else:
            print(0)


if __name__ == "__main__":
    main()
