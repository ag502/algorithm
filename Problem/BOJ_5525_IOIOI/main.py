from sys import stdin

def main():
    n = int(stdin.readline())
    length_of_string = int(stdin.readline())
    s = stdin.readline().rstrip()

    answer = 0
    pattern_cnt = 0
    idx = 1
    while idx <= length_of_string - 2:
        if s[idx - 1] == 'I' and s[idx] == 'O' and s[idx + 1] == 'I':
            pattern_cnt += 1
            if pattern_cnt == n:
                answer += 1
                pattern_cnt -= 1
            idx += 1
        else:
            pattern_cnt = 0
        idx += 1
    print(answer)

if __name__ == '__main__':
    main()