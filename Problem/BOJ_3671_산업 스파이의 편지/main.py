from sys import stdin
from itertools import permutations


def main():
    test_case = int(stdin.readline().rstrip())

    for _ in range(test_case):
        number = int(stdin.readline().rstrip())
        number_list = list(str(number))
        max_value = int(''.join(sorted(number_list, reverse=True)))

        prime_list = [i for i in range(max_value + 1)]
        prime_list[0] = -1
        prime_list[1] = -1

        for i in range(2, int(max_value ** 0.5) + 1):
            for j in range(i * i, len(prime_list), i):
                if prime_list[j] != -1:
                    prime_list[j] = -1

        number_set = set()
        answer = 0
        for i in range(1, len(number_list) + 1):
            per_list = list(permutations(number_list, i))
            for per in per_list:
                number_set.add(int(''.join(per)))
        for cur_number in number_set:
            if prime_list[cur_number] != -1:
                answer += 1
        print(answer)


if __name__ == "__main__":
    main()
