from sys import stdin

def main():
    N = int(stdin.readline().rstrip())
    taller_heights = list(map(int, stdin.readline().split()))
    heights = []

    for i in range(N - 1, -1, -1):
        heights.insert(taller_heights[i], i + 1)

    print(' '.join(map(str, heights)))

if __name__ == '__main__':
    main()