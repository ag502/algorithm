from sys import stdin

# solved with KMP
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
    matched =0
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
    n = int(stdin.readline())
    string_length = int(stdin.readline())
    input_str = stdin.readline().rstrip()

    keyword = []
    for i in range(1, 2 * n + 2):
        if i % 2 == 0:
            keyword.append('O')
        else:
            keyword.append('I')
    keyword = ''.join(keyword)

    pi = get_partial_match(keyword)
    answer = kmp_search(input_str, keyword, pi)
    print(len(answer))

# solved without KMP
# def main():
#     n = int(stdin.readline())
#     length_of_string = int(stdin.readline())
#     s = stdin.readline().rstrip()
#
#     answer = 0
#     pattern_cnt = 0
#     idx = 1
#     while idx <= length_of_string - 2:
#         if s[idx - 1] == 'I' and s[idx] == 'O' and s[idx + 1] == 'I':
#             pattern_cnt += 1
#             if pattern_cnt == n:
#                 answer += 1
#                 pattern_cnt -= 1
#             idx += 1
#         else:
#             pattern_cnt = 0
#         idx += 1
#     print(answer)

if __name__ == '__main__':
    main()