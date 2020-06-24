from sys import stdin

def main():
    r, c = map(int, stdin.readline().split())
    cross_word = [list(stdin.readline().rstrip()) for _ in range(r)]

    answer = []
    for i in range(0, r):
        words = ''.join(cross_word[i]).split('#')
        for word in words:
            if len(word) >= 2:
                answer.append(word)

    for i in range(0, c):
        column_words = ''
        for j in range(0, r):
            column_words += cross_word[j][i]
        column_words = column_words.split('#')
        for word in column_words:
            if len(word) >= 2:
                answer.append(word)

    answer.sort()
    print(answer[0])

if __name__ == "__main__":
    main()