from sys import stdin
from typing import List


def calc_score(num_of_member: int, order_chicken: List[int], scores: List[List[int]]) -> int:
    sum_of_score = 0
    for member in range(num_of_member):
        cur_member_score = 0
        for chicken in order_chicken:
            cur_member_score = max(cur_member_score, scores[member][chicken - 1])
        sum_of_score += cur_member_score
    return sum_of_score


def main() -> None:
    stdin = open("./input.txt", "r")
    num_of_member: int
    num_of_chicken: int
    num_of_member, num_of_chicken = list(map(int, stdin.readline().split()))
    scores: List[List[int]] = []

    for _ in range(num_of_member):
        scores.append(list(map(int, stdin.readline().split())))

    visited: List[bool] = [False] * (num_of_chicken + 1)
    order_chickens: List[List[int]] = []

    def select_chickens(cur_chicken: int, order_chicken: List[int] = []) -> None:
        visited[cur_chicken] = True
        order_chicken.append(cur_chicken)

        if len(order_chicken) < 3:
            for next_chicken in range(cur_chicken, num_of_chicken + 1):
                if not visited[next_chicken]:
                    select_chickens(next_chicken, order_chicken)
        elif len(order_chicken) == 3:
            order_chickens.append(order_chicken[:])
        order_chicken.pop()
        visited[cur_chicken] = False

    for start_chicken in range(1, num_of_chicken + 1):
        select_chickens(start_chicken)

    answer = 0
    for order_chicken in order_chickens:
        answer = max(answer, calc_score(num_of_member, order_chicken, scores))

    print(answer)


if __name__ == '__main__':
    main()