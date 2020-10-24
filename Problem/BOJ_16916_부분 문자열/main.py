from sys import stdin

def get_partial_match(keyword):
    # 시작 점
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
    input_str = stdin.readline().rstrip()
    keyword = stdin.readline().rstrip()

    pi = get_partial_match(keyword)
    answer = kmp_search(input_str, keyword, pi)

    print(1 if len(answer) != 0 else 0)

if __name__ == '__main__':
    main()