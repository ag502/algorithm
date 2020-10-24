from sys import stdin

def combination_with_replacement(cur_num, selected_num, n, str_temp, answer):
    str_temp.append(str(cur_num))
    selected_num += 1

    for next_num in range(3):
        if selected_num != n:
            combination_with_replacement(next_num, selected_num, n, str_temp, answer)
    if len(str_temp) == n:
        answer.append(int(''.join(str_temp)))
    str_temp.pop()
    selected_num -= 1

def main():
    stdin = open('./test_case.txt', 'r')
    n = int(stdin.readline())

    numbers = []
    for i in range(1, 3):
        combination_with_replacement(i, 0, n, [], numbers)

    answer = 0
    for number in numbers:
        if number % 3 == 0:
            answer += 1

    print(answer)

if __name__ == '__main__':
    main()

