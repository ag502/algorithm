from sys import stdin

answer = []

def insert_plus(number):
    operation = []
    for idx, digit in enumerate(number):
        operation.append(digit)
        if idx != len(number) - 1:
            operation.append("+")
    return ''.join(operation)

def dfs(numbers, target_number, temp, cur_number, acc_sum):
    temp.append(cur_number)

    for next_number in numbers:
        if acc_sum + next_number <= target_number:
            dfs(numbers, target_number, temp, next_number, acc_sum + next_number)

    if acc_sum == target_number:
        answer.append(''.join(map(str, temp)))
    temp.pop()

def main():
    stdin = open('./input.txt', 'r')
    n, k = map(int, stdin.readline().split())

    numbers = [1, 2, 3]
    for number in numbers:
        dfs(numbers, n, [], number, number)

    answer.sort()

    if k - 1 >= len(answer):
        print(-1)
    else:
        print(insert_plus(answer[k - 1]))

if __name__ == '__main__':
    main()