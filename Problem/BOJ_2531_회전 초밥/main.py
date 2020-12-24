from sys import stdin
from collections import deque

def main():
    stdin = open('./input.txt', 'r')
    num_of_dishes, num_of_sushi, k, coupon_sushi = map(int, stdin.readline().split())

    sushi_belt = [0] * num_of_dishes
    for idx in range(num_of_dishes):
        sushi_belt[idx] = int(stdin.readline())

    dp = [0] * num_of_dishes
    queue = deque()
    for i in range(k):
        queue.append(sushi_belt[i])
    queue.append(coupon_sushi)
    dp[0] = len(set(queue))
    queue.pop()

    for i in range(1, len(sushi_belt)):
        queue.popleft()
        queue.append(sushi_belt[(i + k - 1) % num_of_dishes])
        queue.append(coupon_sushi)
        dp[i] = len(set(queue))
        queue.pop()

    print(max(dp))

if __name__ == '__main__':
    main()
