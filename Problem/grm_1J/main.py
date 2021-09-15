from sys import stdin

def main():
    stdin = open('Problem\grm_1J\input.txt', 'r')
    n = int(stdin.readline())

    answer = 0
    for i in range(n + 1):
        answer += (i * (i + 1)) // 2

    print(answer)

if __name__ == "__main__":
    main()