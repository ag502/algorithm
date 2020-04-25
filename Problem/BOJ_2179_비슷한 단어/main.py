from sys import stdin

def main():
    n = int(stdin.readline())

    word_dict = {}

    for i in range(n):
        word_dict[i] = stdin.readline().rstrip()
    word_dict = sorted(word_dict.items(), key=lambda x: x[1])

    overlapped_word_count = 0
    answer_word_idx = 0
    answer_word = word_dict[0][1] + '\n' + word_dict[1][1]

    for idx in range(len(word_dict) - 1):
        current_word = word_dict[idx][1]
        next_word = word_dict[idx + 1][1]
        min_word_len = min(len(current_word), len(next_word))
        temp = 0

        for i in range(min_word_len):
            if current_word[i] != next_word[i]:
                break
            else:
                temp += 1

        if temp > overlapped_word_count:
            overlapped_word_count = temp
            answer_word_idx = word_dict[idx][0]
            answer_word = current_word + '\n' + next_word
        elif temp == overlapped_word_count:
            if answer_word_idx >= word_dict[idx][0]:
                answer_word_idx = word_dict[idx][0]
                answer_word = current_word + '\n' + next_word


    print(answer_word)
    print(word_dict)

if __name__ == "__main__":
    main()

