from sys import stdin

def main():
    stdin = open('./test_case.txt', 'r')
    number = list(map(int, list(stdin.readline().strip())))
    count = 0
    while len(number) > 1:
        count += 1
        number = list(map(int, list(str(sum(number)))))

    print(count)
    if number [0] in [3, 6, 9]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()