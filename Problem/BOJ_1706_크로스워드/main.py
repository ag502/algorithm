from sys import stdin

def main():
    r, c = list(map(int, stdin.readline().split()))
    cross_word = [stdin.readline().rstrip() for _ in range(r)]
    word_list = []

    # 가로낱말
    for word in cross_word:
        if '#' not in word:
            word_list.append(word)
        else:
            temp = word.split('#')
            for sub_word in temp:
                if len(sub_word) > 1:
                    word_list.append(sub_word)

    # 세로낱말
    for i in range(c):
        temp_string = ''
        for j in range(r):
            current_alphabet = cross_word[j][i]

            if current_alphabet == '#':
                if len(temp_string) > 1:
                    word_list.append(temp_string)
                temp_string = ''
            else:
                temp_string += current_alphabet
        if len(temp_string) > 1:
            word_list.append(temp_string)

    word_list.sort()
    print(word_list[0])

if __name__ == "__main__":
    main()
