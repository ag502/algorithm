from sys import stdin

def get_partial_matched(keyword):
    begin, matched = [1, 0]
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
    begin, matched = [0, 0]
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
    is_visited = [False] * len(input_string)

    n = int(stdin.readline())
    keywords = []

    for _ in range(n):
        keywords.append(stdin.readline().rstrip())

    for keyword in keywords:
        pi = get_partial_matched(keyword)
        answer = kmp_search(input_string, keyword, pi)
        

if __name__ == '__main__':
    main()