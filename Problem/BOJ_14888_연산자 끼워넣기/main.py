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

def dfs(operators, visited, start_idx, answer, temp):
    # 1. 방문
    visited[start_idx] = True
    # 2. 도착
    temp.append(operators[start_idx])
    # 3. 주변 탐색
    for next_idx in range(len(operators)):
        # 4. 갈 수 있는지 확인
        if not visited[next_idx]:
            dfs(operators, visited, next_idx, answer, temp)
    # 5. 체크아웃
    if len(temp) == len(operators):
        answer.append(''.join(temp))
    # visited[start_idx] = False
    temp.pop()

def main():
    stdin = open('./test_case.txt', 'r')

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


    # backtracking
    visited = [False] * len(operator_list)
    # print(operator_list)
    # print(visited)
    permute = []
    for idx in range(len(operator_list)):
        dfs(operator_list, visited, idx, permute, [])

    permute = set(permute)
    print(permute)

    max_res = -1000000001
    min_res = 1000000001
    for operator in permute:
        operator = list(operator)
        result = do_operation(numbers[0], numbers[1], operator[0])
        for i in range(1, len(operator)):
            result = do_operation(result, numbers[i + 1], operator[i])
        if max_res < result:
            max_res = result
        if min_res > result:
            min_res = result

    # python permutation
    # operator_list = set(permutations(operator_list))
    # max_res = -1000000001
    # min_res = 1000000001
    # for operator in operator_list:
    #     result = do_operation(numbers[0], numbers[1], operator[0])
    #     for i in range(1, len(operator)):
    #         result = do_operation(result, numbers[i + 1], operator[i])
    #     if max_res < result:
    #         max_res = result
    #     if min_res > result:
    #         min_res = result

    print(max_res)
    print(min_res)

if __name__ == '__main__':
    main()
