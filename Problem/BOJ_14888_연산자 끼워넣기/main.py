from sys import stdin
from itertools import permutations

def do_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    else:
        if num1 < 0:
            return -(-num1 // num2)
        else:
            return num1 // num2


def main():
    n = int(stdin.readline())
    numbers = list(map(int, stdin.readline().split()))
    operators = list(map(int, stdin.readline().split()))
    operator_list = []
    for idx, operator in enumerate(operators):
        if idx == 0:
            operator_list += ['+'] * operator
        elif idx == 1:
            operator_list += ['-'] * operator
        elif idx == 2:
            operator_list += ['*'] * operator
        else:
            operator_list += ['/'] * operator

    operator_list = set(permutations(operator_list))
    max_res = -1000000001
    min_res = 1000000001
    for operator in operator_list:
        result = do_operation(numbers[0], numbers[1], operator[0])
        for i in range(1, len(operator)):
            result = do_operation(result, numbers[i + 1], operator[i])
        if max_res < result:
            max_res = result
        if min_res > result:
            min_res = result

    print(max_res)
    print(min_res)

if __name__ == '__main__':
    main()
