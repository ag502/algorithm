from sys import stdin

def short_power(a, b, c):
    if b == 0:
        return 1
    answer = short_power(a, b // 2, c)
    answer = (answer * answer) % c

    if b % 2 != 0:
        answer = (answer * a) % c
    return answer

def main():
    a, b, c = map(int, stdin.readline().split())
    print(short_power(a, b, c))

if __name__ == "__main__":
    main()