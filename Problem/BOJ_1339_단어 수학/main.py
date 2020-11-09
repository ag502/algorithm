from sys import stdin

def main():
    stdin = open('./test_case.txt', 'r')
    num_of_word = int(stdin.readline())

    table = {}
    for _ in range(num_of_word):
        word = list(stdin.readline().rstrip())

        for idx in range(len(word)):
            if word[idx] not in table:
                table[word[idx]] = 0
            table[word[idx]] += 10 ** (len(word) - 1 - idx)

    table = sorted(table.items(), key=lambda x: -x[1])
    numbers = [i for i in range(9, 9 - len(table), -1)]

    answer = 0
    for idx in range(len(table)):
        answer += table[idx][1] * numbers[idx]
    print(answer)

if __name__ == '__main__':
    main()