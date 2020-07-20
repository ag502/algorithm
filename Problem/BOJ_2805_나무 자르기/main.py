from sys import stdin


def main():
    n, m = map(int, stdin.readline().split())
    trees = sorted(list(map(int, stdin.readline().split())))
    # heights = [i for i in range(max(trees) + 1)]

    start = 0
    end = max(trees)
    candidate_height = []
    while start <= end:
        mid = (start + end) // 2
        sum_of_cut = sum([tree - mid if tree -
                          mid > 0 else 0 for tree in trees])

        if sum_of_cut == m:
            print(mid)
            return
        elif sum_of_cut > m:
            start = mid + 1
            candidate_height.append(mid)
        elif sum_of_cut < m:
            end = mid - 1

    print(max(candidate_height))


if __name__ == "__main__":
    main()
