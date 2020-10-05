from sys import stdin

chars = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         ]
def main():
    n = int(stdin.readline())
    graph = [[float('inf')] * 53 for _ in range(53)]
    for i in range(1, 53):
        graph[i][i] = 0

    for _ in range(n):
        proposition = [char.strip() for char in stdin.readline().split("=>")]
        front = -1
        back = -1
        if 'A' <= proposition[0] <= 'Z':
            front = ord(proposition[0]) - 64
        elif 'a' <= proposition[0] <= 'z':
            front = ord(proposition[0]) - 70

        if 'A' <= proposition[1] <= 'Z':
            back = ord(proposition[1]) - 64
        elif 'a' <= proposition[1] <= 'z':
            back = ord(proposition[1]) - 70

        graph[front][back] = 1

    # Floyd-Warshall
    for k in range(1, 53):
        for i in range(1, 53):
            for j in range(1, 53):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


    answer = set()
    for i in range(1, 53):
        for j in range(1, 53):
            if graph[i][j] != float('inf') and i != j:
                answer.add(chars[i] + " => " + chars[j])

    answer = sorted(answer)
    print(len(answer))
    for proposition in answer:
        print(proposition)


if __name__ == '__main__':
    main()