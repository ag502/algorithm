from sys import stdin

def make_tree(sequence, depth, answer):
    if len(sequence) == 1:
        answer[depth].append(sequence[0])
        return
    mid = len(sequence) // 2
    answer[depth].append(sequence[mid])
    make_tree(sequence[0:mid], depth + 1, answer)
    make_tree(sequence[mid + 1:], depth + 1, answer)

def main():
    stdin = open('./input.txt', 'r')
    depth = int(stdin.readline())
    visit_seq = list(map(int, stdin.readline().split()))

    answer = {}
    for i in range(1, depth + 1):
        answer[i] = []
    make_tree(visit_seq, 1, answer)

    for depth in answer.keys():
        print(' '.join(map(str, answer[depth])))

if __name__ == '__main__':
    main()
