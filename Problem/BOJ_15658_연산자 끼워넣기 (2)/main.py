from sys import stdin, maxsize

operators = {"+": 0, "-": 1, "*": 2, "/": 3}


def do_operate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "*":
        return num1 * num2
    elif operator == "-":
        return num1 - num2
    elif operator == "/":
        if num1 < 0:
            return -(-num1 // num2)
        else:
            return num1 // num2


def dfs(numbers, num_of_operators, cur_idx, operator, acc_num, value, count):
    cur_number = numbers[cur_idx]
    if cur_idx != 0:
        acc_num = do_operate(acc_num, cur_number, operator)
    else:
        acc_num = cur_number

    for next_idx in range(cur_idx + 1, len(numbers)):
        for next_op, idx in operators.items():
            if num_of_operators[idx] > 0 and count < len(numbers):
                num_of_operators[idx] -= 1
                dfs(numbers, num_of_operators, next_idx, next_op, acc_num, value, count + 1)

    if count == len(numbers):
        value.append(acc_num)

    if cur_idx != 0:
        num_of_operators[operators[operator]] += 1


def main():
    stdin = open("./input.txt", "r")
    num_of_numbers = int(stdin.readline())

    numbers = list(map(int, stdin.readline().split()))
    num_of_operators = list(map(int, stdin.readline().split()))

    value = []
    dfs(numbers, num_of_operators, 0, "", 0, value, 1)

    print(max(value))
    print(min(value))


if __name__ == '__main__':
    main()