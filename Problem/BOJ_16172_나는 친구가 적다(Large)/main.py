from sys import stdin

def get_partial_match(keyword):
    begin = 1
    matched = 0
    pi = [0] * (len(keyword) + 1)
    while begin + matched < len(keyword):
        if keyword[begin + matched] == keyword[matched]:
            matched += 1
            pi[begin + matched] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched]
                matched = pi[matched]

    return pi


def kmp_search(input_str, keyword, pi):
    begin = 0
    matched = 0
    answer = []

    while begin <= len(input_str) - len(keyword):
        if matched < len(keyword) and input_str[begin + matched] == keyword[matched]:
            matched += 1
            if matched == len(keyword):
                answer.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched]
                matched = pi[matched]
    return answer

def main():
    stdin = open('./test_case.txt', 'r')
    input_string = stdin.readline().rstrip()
    keyword = stdin.readline().rstrip()

    processed_str = []
    for char in input_string:
        if '0' <= char <= '9':
            continue
        processed_str.append(char)
    processed_str = ''.join(processed_str)

    pi = get_partial_match(keyword)
    begin_indexes = kmp_search(processed_str, keyword, pi)

    if len(begin_indexes) != 0:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()