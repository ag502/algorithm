from sys import stdin

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def dfs(n, cur_number, answer, temp):
    # 1. 도착
    temp.append(cur_number)
    # 2. 주변 탐색
    for next_number in range(0, 10):
        # 3. 갈 수 있는지 검사
        if is_prime(int(''.join(map(str, temp))) * 10 + next_number):
            dfs(n, next_number, answer, temp)
    # 4. checkout
    if len(temp) == n:
        answer.append(''.join(map(str, temp)))
    temp.pop()

def main():
    stdin = open('./test_case.txt', 'r')
    n = int(stdin.readline())
    numbers = [i for i in range(0, 10)]

    answer = []
    for i in range(0, 10):
        if is_prime(i):
            dfs(n, i, answer, [])

    answer.sort()

    for prime in answer:
        print(prime)

if __name__ == '__main__':
    main()