from sys import stdin

def dfs(number, visited, sequence, temp, cur_num):
    # 방문
    visited[cur_num] = True
    temp.append(cur_num)
    # 주변 탐색
    for next_num in range(1, number + 1):
        if not visited[next_num] and len(temp) != number:
            dfs(number, visited, sequence, temp, next_num)
    # 체크아웃
    if len(temp) == number:
        sequence.append(' '.join(map(str, temp)))
    temp.pop()
    visited[cur_num] = False

def main():
    stdin = open('./input.txt', 'r')
    number = int(stdin.readline())

    visited = [False] * (number + 1)
    sequence = []

    for num in range(1, number + 1):
        dfs(number, visited, sequence, [], num)

    for seq in sequence:
        print(seq)

if __name__ == '__main__':
    main()
