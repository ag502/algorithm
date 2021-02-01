from sys import stdin


def combination(card_numbers, answer, temp, cur_idx):
    temp.append(card_numbers[cur_idx])

    for next_idx in range(cur_idx + 1, len(card_numbers)):
        if len(temp) < 6:
            combination(card_numbers, answer, temp, next_idx)

    if len(temp) == 6:
        answer.append(temp[:])
    temp.pop()


def main():
    stdin = open("input.txt", "r")

    count = 0
    while True:
        numbers = list(map(int, stdin.readline().split()))

        if numbers[0] == 0:
            break

        if count != 0:
            print()

        count += 1
        card_numbers = sorted(numbers[1:])

        answer = []
        for i in range(len(card_numbers)):
            combination(card_numbers, answer, [], i)

        for card_comb in answer:
            print(' '.join(map(str, card_comb)))


if __name__ == '__main__':
    main()