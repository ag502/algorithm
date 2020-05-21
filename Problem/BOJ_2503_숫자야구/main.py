from sys import stdin
from collections import Counter

def isStrike(number, strike, ball, number_list):
    answer = list(str(number))
    for idx, number in enumerate(number_list):
        compare_number = list(str(number))
        if sorted(Counter(compare_number).items(), key=lambda x: -x[1])[0][1] >= 2 \
                or '0' in compare_number:
            number_list[idx] = -1
            continue

        temp_strike = 0
        temp_ball = 0
        if number == -1:
            continue
        else:
            for answer_digit, compare_digit in zip(answer, compare_number):
                if answer_digit == compare_digit:
                    temp_strike += 1
                elif compare_digit in answer:
                    temp_ball += 1
        if temp_strike != strike or temp_ball != ball:
            number_list[idx] = -1



def main():
    n = int(stdin.readline())
    number_list = [i for i in range(123, 988)]

    for _ in range(n):
        answer, strike, ball = map(int, stdin.readline().split())
        isStrike(answer, strike, ball, number_list)

    result = 0
    for number, counter in Counter(number_list).items():
        if number != -1:
            result += 1
    print(result)


if __name__ == "__main__":
    main()