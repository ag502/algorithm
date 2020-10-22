from sys import stdin

def main():
    stdin = open('./test_case.txt', 'r')
    n, a, d = map(int, stdin.readline().split())
    notes = list(map(int, stdin.readline().split()))

    answer = 0
    for note in notes:
        if note == a:
            answer += 1
            a += d

    print(answer)

if __name__ == '__main__':
    main()