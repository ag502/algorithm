from sys import stdin

def main():
    while True:
        n = int(stdin.readline())
        if n == 0:
            break
        number_list = [i for i in range(0, 2 * n + 1)]
        m = int((2 * n) ** 0.5) + 1
        for i in range(2, m):
            if number_list[i] != -1:
                for j in range(i + i, 2 * n + 1, i):
                    number_list[j] = -1

        answer = 0
        for i in range(n + 1, len(number_list)):
            if number_list[i] != -1:
                answer += 1

        print(answer)

if __name__ == "__main__":
    main()