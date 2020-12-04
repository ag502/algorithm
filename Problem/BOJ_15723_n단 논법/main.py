from sys import stdin

def convertCharToInt (char):
    return ord(char.strip()) - ord('a')

def main():
    stdin = open('./input.txt', 'r')
    num_of_presumes = int(stdin.readline())

    dist = [[float('inf')] * 26 for _ in range(26)]
    for i in range(26):
        dist[i][i] = 0

    for _ in range(num_of_presumes):
        presume, conclusion = stdin.readline().rstrip().split('is')
        dist[convertCharToInt(presume)][convertCharToInt(conclusion)] = 1


    for k in range(26):
        for i in range(26):
            for j in range(26):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    num_of_conclusions = int(stdin.readline())
    for _ in range(num_of_conclusions):
        presume, conclusion = stdin.readline().rstrip().split('is')
        if dist[convertCharToInt(presume)][convertCharToInt(conclusion)] != 0 and \
            dist[convertCharToInt(presume)][convertCharToInt(conclusion)] != float('inf'):
            print('T')
        else:
            print('F')

if __name__ == '__main__':
    main()
