from sys import stdin

stdin = open("./input.txt", "r")
num_of_thing = int(stdin.readline())
num_of_relation = int(stdin.readline())

weights = [[float("INF")] * (num_of_thing + 1) for _ in range(num_of_thing + 1)]

for i in range(num_of_thing + 1):
    weights[i][i] = 0

for _ in range(num_of_relation):
    thing1, thing2 = map(int, stdin.readline().split())
    weights[thing1][thing2] = 1


def main():
    for k in range(num_of_thing + 1):
        for i in range(num_of_thing + 1):
            if weights[i][k] == float("INF"):
                continue
            for j in range(num_of_thing + 1):
                weights[i][j] = min(weights[i][k] + weights[k][j], weights[i][j])

    # for row in weights:
    #     print(row)

    for thing1 in range(1, num_of_thing + 1):
        answer = 0
        for thing2 in range(1, num_of_thing + 1):
            if weights[thing1][thing2] == float("INF") and weights[thing2][thing1] == float("INF"):
                answer += 1
        print(answer)


if __name__ == '__main__':
    main()