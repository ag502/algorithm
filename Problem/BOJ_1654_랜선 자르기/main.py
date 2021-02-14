from sys import stdin


def cut_lan(cur_length):
    num_of_lan = 0
    for lan in lans:
        num_of_lan += lan // cur_length
    return num_of_lan


def binary_search():
    start = 1
    end = max(lans)

    while start <= end:
        mid = (start + end) // 2
        num_of_lan = cut_lan(mid)
        if num_of_lan < n:
            end = mid - 1
        elif num_of_lan >= n:
            start = mid + 1
    return end


def main():
    stdin = open('./input.txt', 'r')
    global k, n, lans
    lans = []
    k, n = map(int, stdin.readline().split())

    for _ in range(k):
        lans.append(int(stdin.readline()))
    lans.sort()

    print(binary_search())


if __name__ == '__main__':
    main()