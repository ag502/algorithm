from sys import stdin

def get_partial_match(template):
    begin = 1
    matched = 0
    pi = [0] * (len(template) + 1)
    while begin + matched < len(template):
        if template[begin + matched] == template[matched]:
            matched += 1
            pi[begin + matched] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched]
                matched = pi[matched]
    return pi

def kmp_search(target_str, template, pi):
    begin = 0
    matched = 0
    answer = []

    while begin <= len(target_str) - len(template):
        if matched < len(template) and target_str[begin + matched] == template[matched]:
            matched += 1
            if matched == len(template):
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
    str_1 = stdin.readline().rstrip()
    str_2 = stdin.readline().rstrip()
    template = stdin.readline().rstrip()

    pi = get_partial_match(template)

    answer_1 = kmp_search(str_1, template, pi)
    answer_2 = kmp_search(str_2, template, pi)

    if len(answer_1) != 0 and len(answer_2) != 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()