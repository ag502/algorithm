from sys import stdin

def main():
    N = int(stdin.readline().rstrip())
    weight_heights = []
    rank = [1] * N

    for _ in range(N):
        weight_heights.append(list(map(int, stdin.readline().split())))

    for i in range(N):
        for j in range(N):
            if weight_heights[i][0] < weight_heights[j][0] and weight_heights[i][1] < weight_heights[j][1]:
                rank[i] += 1

    print(' '.join(map(str, rank)))

if __name__ == '__main__':
    main()