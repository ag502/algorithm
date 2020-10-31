from sys import stdin

def dfs(cur_num, answer, temp):
    # 1. 도착
    temp.append(cur_num)

    # 2. 탐색
    for next_number in range(0, 10):
        # 3. 갈 수 있는지 검사
        if temp[len(temp) - 1] > next_number:
            answer.append(int(''.join(map(str, temp)) + str(next_number)))
            dfs(next_number, answer, temp)

    # 4. 체크아웃
    temp.pop()

def main():
    stdin = open('./test_case.txt', 'r')
    n = int(stdin.readline())
    numbers = [i for i in range(0, 10)]

    for number in range(1, 10):
        dfs(number, numbers, [])

    numbers.sort()
    try:
        print(numbers[n])
    except:
        print(-1)

if __name__ == '__main__':
    main()
