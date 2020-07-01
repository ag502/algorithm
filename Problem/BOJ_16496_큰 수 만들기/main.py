from sys import stdin
from functools import cmp_to_key

def sort_num_string_list(a, b):
    num_1 = int(a + b)
    num_2 = int(b + a)
    return num_2 - num_1

def main():
    num_of_number = int(stdin.readline())
    number_list = list(stdin.readline().split())

    number_list = sorted(number_list, key=cmp_to_key(sort_num_string_list))
    answer = ''.join(number_list)

    if answer[0] == '0':
        print(0)
    else:
        print(answer)

if __name__ == '__main__':
    main()