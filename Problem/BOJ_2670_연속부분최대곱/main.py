from sys import stdin

def main():
    stdin = open('./input.txt', 'r')
    num_of_floats = int(stdin.readline())

    floats = []
    for _ in range(num_of_floats):
        floats.append(float(stdin.readline()))

    dp = floats[:]
    for idx in range(1, num_of_floats):
        dp[idx] = max(dp[idx - 1] * floats[idx], floats[idx])

    # print(floats)
    # print(dp)
    print('{:.3f}'.format(max(dp)))

if __name__ == '__main__':
    main()