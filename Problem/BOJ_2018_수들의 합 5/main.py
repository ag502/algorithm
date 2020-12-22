from sys import stdin

def main():
    stdin = open('./input.txt', 'r')
    target_number = int(stdin.readline())

    k = 1
    answer = 0
    while True:
        temp = (k * (k + 1)) / 2
        if target_number - temp < 0:
            break
        if (target_number - temp) % k == 0:
            answer += 1
        k += 1

    print(answer)

if __name__ == '__main__':
    main()