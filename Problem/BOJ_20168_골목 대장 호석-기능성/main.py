from sys import stdin
from collections import deque

def dfs(intersections, visited, cur_money, cur_ic, finish_ic, lost_money, answer):
    # 1. 방문
    visited[cur_ic] = True

    # 2. 주변 탐색
    if cur_ic != finish_ic:
        for next_money, next_ic in intersections[cur_ic]:
            if cur_money >= sum(lost_money) + next_money and not visited[next_ic]:
                lost_money.append(next_money)
                dfs(intersections, visited, cur_money, next_ic, finish_ic, lost_money, answer)
    elif cur_ic == finish_ic:
        answer.append(max(lost_money))
    if len(lost_money) != 0:
        lost_money.pop()
    visited[cur_ic] = False

def main():
    stdin = open('./input.txt', 'r')
    num_of_ic, num_of_roads, start_ic, finish_ic, cur_money = map(int, stdin.readline().split())

    intersections = {}
    for ic in range(1, num_of_ic + 1):
        intersections[ic] = []

    for _ in range(num_of_roads):
        ic_1, ic_2, required_money = map(int, stdin.readline().split())
        intersections[ic_1].append([required_money, ic_2])
        intersections[ic_2].append([required_money, ic_1])

    answer = []
    visited = [False] * (num_of_ic + 1)
    dfs(intersections, visited, cur_money, start_ic, finish_ic, deque(), answer)

    if len(answer) == 0:
        print(-1)
    else:
        print(min(answer))
if __name__ == '__main__':
    main()