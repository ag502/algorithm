from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    social_network = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        social_network[i][i] = 0

    for _ in range(m):
        person1, person2 = map(int, stdin.readline().split())
        social_network[person1][person2] = 1
        social_network[person2][person1] = 1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if social_network[i][k] == float('inf'):
                continue
            for j in range(1, n + 1):
                social_network[i][j] = min(social_network[i][j], social_network[i][k] + social_network[k][j])

    answer = []
    for person in range(1, n + 1):
        total_length = 0
        for friend in range(1, n + 1):
            total_length += social_network[person][friend]
        answer.append((person, total_length))

    answer = sorted(answer, key=lambda x: (x[1], x[0]))
    print(answer[0][0])

if __name__ == '__main__':
    main()