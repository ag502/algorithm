from sys import stdin
from itertools import permutations

def string_to_num(string):
    return int(''.join(string))

def is_prime(number):
    prime_list = set()
    number_list = [i for i in range(0, number + 1)]
    for i in range(2, int(number ** 0.5) + 1):
        start_index = i * 2
        interval = 2
        while start_index <= number:
            interval += 1
            if number_list[start_index] != -1:
                number_list[start_index] = -1
            start_index = i * interval
    number_list.sort(reverse=True)
    for num in number_list:
        # if number_list[idx] != -1:
        #     prime_list.add(number_list[idx])
        if num != 1:
            prime_list.add(num)
        else:
            break
    # print(number_list)
    return prime_list

def main():
    test_case = int(stdin.readline())
    for _ in range(test_case):
        number_str = list(stdin.readline().rstrip())
        number_set = set()
        for i in range(1, len(number_str) + 1):
            # number_set = set(list(map(string_to_num, permutations(number_str, i))))
            number_list = list(map(string_to_num, permutations(number_str, i)))
            print(set(number_list))
            for num in number_list:
                number_set.add(num)

        prime_list = is_prime(max(number_set))
        num_of_prime = 0
        for num in prime_list:
            if num in number_set:
                num_of_prime += 1
        print(number_set)
        print(num_of_prime)

if __name__ == '__main__':
    main()
