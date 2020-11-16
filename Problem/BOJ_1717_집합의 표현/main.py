from sys import stdin

def find(num, parents):
    if parents[num] == num:
        return num
    parents[num] = find(parents[num], parents)
    return parents[num]

def merge(num1, num2, parents, ranks):
    num1_root = find(num1, parents)
    num2_root = find(num2, parents)

    if num1_root == num2_root:
        return

    if ranks[num2_root] > ranks[num1_root]:
        temp = ranks[num1_root]
        ranks[num1_root] = ranks[num2_root]
        ranks[num2_root] = temp

    parents[num2_root] = num1_root

    if ranks[num1_root] == ranks[num2_root]:
        ranks[num1_root] += 1

def main():
    stdin = open('./test_case.txt', 'r')
    n, m = map(int, stdin.readline().split())
    parents = [i for i in range(n + 1)]
    ranks = [0] * (n + 1)

    for _ in range(m):
        operation, num1, num2 = map(int, stdin.readline().split())

        if operation == 0:
            merge(num1, num2, parents, ranks)
        elif operation == 1:
            if num1 == num2:
                print('YES')
            elif find(num1, parents) == find(num2, parents):
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    main()

