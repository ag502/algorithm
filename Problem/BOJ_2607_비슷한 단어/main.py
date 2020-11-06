from sys import stdin
from collections import Counter

def is_similar_word(standard, word):
    # 1. 교환
    if len(standard) == len(word):
        standard = Counter(standard)
        word = Counter(word)
        is_different = False
        for standard_char, count in standard.items():
            # 처음 다른 글자
            if not is_different and count != word[standard_char]:
                is_different = True
            elif not is_different and standard_char not in word:
                is_different = True
            # 두번째 이상 다른 글자
            elif is_different and (standard_char not in word or count != word[standard_char]):
                return False
        return True
    # 2. 추가
    elif len(word) - len(standard) == 1:
        standard = Counter(standard)
        word = Counter(word)
        is_different = False
        for word_char, count in word.items():
            # 글자가 첫번째 단어에 없을 때
            if word_char not in standard:
                if count != 1:
                    return False
                is_different = True
            else:
                if not is_different and count != standard[word_char]:
                    # 글자와 첫번째 단어의 글자 수의 차이가 2 이상
                    if abs(count - standard[word_char]) != 1:
                        return False
                    is_different = True
                elif is_different and count != standard[word_char]:
                    return False
        return True
    # 삭제
    elif len(standard) - len(word) == 1:
        standard = Counter(standard)
        word = Counter(word)
        is_different = False
        for standard_char, count in standard.items():
            # 첫번째 단어의 글자가 단어에 없을 때
            if standard_char not in word:
                if count != 1:
                    return False
                is_different = True
            else:
                if not is_different and count != word[standard_char]:
                    if abs(count - word[standard_char]) != 1:
                        return False
                    is_different = True
                elif is_different and count != word[standard_char]:
                    return False
        return True
    return False

def main():
    stdin = open('./test_case.txt', 'r')
    num_of_word = int(stdin.readline())
    first_word = stdin.readline().rstrip()

    answer = 0
    for _ in range(num_of_word - 1):
        word = stdin.readline().rstrip()
        # print(word, is_similar_word(first_word, word))
        if is_similar_word(first_word, word):
            answer += 1
    print(answer)

if __name__ == '__main__':
    main()