from sys import stdin


def permutation(digits, target_number, visited, cur_idx, cur_number_len, temp, answer):
    cur_digit = digits[cur_idx]
    temp.append(cur_digit)
    visited[cur_idx] = True

    for next_idx in range(len(digits)):
        if len(temp) < len(str(target_number)) and not visited[next_idx]:
            permutation(digits, target_number, visited, next_idx, cur_number_len + 1, temp, answer)

    if len(temp) == len(str(target_number)):
        if int(''.join(map(str, temp))) > target_number:
            answer.append(int(''.join(map(str, temp))))

    temp.pop()
    visited[cur_idx] = False


def main():
    stdin = open("./input.txt", "r")
    number = stdin.readline().rstrip()
    digits = list(map(int, list(number)))
    digits.sort()

    answer = []
    for idx in range(len(digits)):
        visited = [False] * len(digits)
        permutation(digits, int(number), visited, idx, 1, [], answer)

    if len(answer) == 0:
        print(0)
    else:
        print(min(answer))


if __name__ == '__main__':
    main()
