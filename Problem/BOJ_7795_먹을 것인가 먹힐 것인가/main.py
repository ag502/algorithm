from sys import stdin

def binary_search(array, target):
    start = 0
    end = len(array) - 1

    target_idx = - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return target_idx if target_idx != -1 else start

def main():
    stdin = open('./input.txt', 'r')
    test_case = int(stdin.readline())

    for _ in range(test_case):
        num_of_a_sp, num_of_b_sp = map(int, stdin.readline().split())
        a_list = list(map(int, stdin.readline().split()))
        b_list = list(map(int, stdin.readline().split()))

        b_list.sort()

        answer = 0
        for a in a_list:
            idx = binary_search(b_list, a)
            if idx > 0:
                answer += idx
        print(answer)

if __name__ == '__main__':
    main()