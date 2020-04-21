from sys import stdin
from collections import Counter


def main():
    word = stdin.readline().rstrip()
    word_counter = Counter(word)
    word_length = len(word)

    odd_number_count = 0
    for word in word_counter:
        if word_length % 2 == 0 and word_counter[word] % 2 == 1:
            print("I'm Sorry Hansoo")
            return
        if word_length % 2 == 1:
            if word_counter[word] % 2 == 1:
                odd_number_count += 1
            if odd_number_count > 1:
                print("I'm Sorry Hansoo")
                return

    word_counter = sorted(word_counter.items(), key=lambda x: x[0])

    front_str = ''
    mid_str = ''

    for word, count in word_counter:
        if count % 2 == 0:
            for _ in range(count//2):
                front_str += '{}'.format(word)
        if count % 2 == 1:
            for _ in range((count - 1)//2):
                front_str += '{}'.format(word)
            mid_str += '{}'.format(word)
    front_str = ''.join(sorted(front_str))
    end_str = ''.join(reversed(front_str))

    print(front_str + mid_str + end_str)


if __name__ == "__main__":
    main()