from sys import stdin


def check_odd(number):
    count = 0
    for digit in number:
        if int(digit) % 2 != 0:
            count += 1
    return count


def process_number(number, count, answer):
    if len(number) == 1:
        answer.append(count + check_odd(number))
    elif len(number) == 2:
        num_of_odds = check_odd(number)
        new_number = int(number[0]) + int(number[1])
        process_number(str(new_number), count + num_of_odds, answer)
    else:
        num_of_odds = check_odd(number)
        for i in range(len(number) - 2):
            for j in range(i + 1, len(number) - 1):
                new_number = int(number[:i + 1]) + int(number[i + 1:j + 1]) + int(number[j + 1:])
                process_number(str(new_number), count + num_of_odds, answer)


def main():
    stdin = open("./input.txt", "r")
    number = stdin.readline().rstrip()

    answer = []
    process_number(number, 0, answer)

    answer.sort()
    print(' '.join([str(answer[0]), str(answer[len(answer) - 1])]))


if __name__ == '__main__':
    main()