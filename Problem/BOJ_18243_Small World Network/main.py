from sys import stdin

def main():
    n, k = map(int, stdin.readline().split())
    world = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    for _ in range(k):
        person1, person2 = map(int, stdin.readline().split())
        world[person1][person2] = 1
        world[person2][person1] = 1

    for i in range(len(world)):
        world[i][i] = 0

    # Floyd-Warshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if world[i][k] == float('inf'):
                continue
            for j in range(1, n + 1):
                world[i][j] = min(world[i][j], world[i][k] + world[k][j])

    for i in range(1, len(world)):
        for j in range(1, len(world[i])):
            if world[i][j] > 6:
                print("Big World!")
                return
    print("Small World!")

if __name__ == '__main__':
    main()