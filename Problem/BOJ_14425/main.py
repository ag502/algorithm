from sys import stdin

def main():
    # stdin = open("./test_case.txt", "r")
    n, m = map(int, stdin.readline().split())
    string_set = set()

    for _ in range(n):
        string_set.add(stdin.readline().rstrip())

    answer = 0

    for _ in range(m):
        if stdin.readline().rstrip() in string_set:
            answer += 1

    print(answer)

if __name__ == '__main__':
    main()