from sys import stdin
from collections import deque

def process_function(func_list, number_deque):
    is_reverse = False
    for function in func_list:
        if function == 'R':
            is_reverse = not is_reverse

        if function == 'D':
            if len(number_deque) == 0:
                return 'error'
            elif is_reverse:
                number_deque.pop()
            elif not is_reverse:
                number_deque.popleft()
    result = ''
    while number_deque:
        if is_reverse:
            result += number_deque.pop() + " "
        else:
            result += number_deque.popleft() + " "
    return '[' + ','.join(list(result.rstrip().split())) + ']'

def make_deque(number_list):
    number_deque = deque()
    for num in number_list:
        if num == '':
            continue
        number_deque.append(num)
    return number_deque

def main():
    test_case = int(stdin.readline())

    for _ in range(test_case):
        function_list = stdin.readline().rstrip()
        length_of_number = int(stdin.readline())
        number_list = stdin.readline().rstrip()
        number_list = number_list[1:len(number_list) - 1].split(',')

        number_deque = make_deque(number_list)
        result = process_function(function_list, number_deque)

        print(result)

if __name__ == '__main__':
    main()