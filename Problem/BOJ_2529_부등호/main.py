from sys import stdin

def process_number(length, number):
    str_number = str(number)
    if len(str_number) != length:
        return '0' + str_number
    return str_number

def compare(num1, num2, sign):
    if sign == "<":
        return num1 < num2
    else:
        return num1 > num2

def dfs(length, signs, visited, answer, temp, cur_number):
    # 방문
    visited[cur_number] = True
    temp.append(cur_number)
    # 주변 탐색
    for next_number in range(0, 10):
        if not visited[next_number] and len(temp) != length:
            if compare(cur_number, next_number, signs[len(temp) - 1]):
                dfs(length, signs, visited, answer, temp, next_number)
    if len(temp) == length:
        answer.append(int(''.join(map(str, temp))))
    temp.pop()
    visited[cur_number] = False


def main():
    stdin = open('./input.txt', 'r')
    num_of_sign = int(stdin.readline())
    signs = stdin.readline().split()

    answer = []
    for number in range(0, 10):
        visited = [False] * 10
        dfs(num_of_sign + 1, signs, visited, answer, [], number)

    max_value = max(answer)
    min_value = min(answer)

    print(process_number(num_of_sign + 1, max_value))
    print(process_number(num_of_sign + 1, min_value))

if __name__ == '__main__':
    main()