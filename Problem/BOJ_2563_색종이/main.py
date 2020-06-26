from sys import stdin

def overlap_area(pos1, pos2):
    overlap_x = min(pos1[0], pos2[0]) + 10 - max(pos1[0], pos2[0])
    overlap_y = min(pos1[1], pos2[1]) + 10 - max(pos1[1], pos2[1])

    return 0 if overlap_x * overlap_y < 0 else overlap_x * overlap_y

def main():
    n = int(stdin.readline())
    position_list = [tuple(map(int,stdin.readline().split())) for _ in range(n)]

    overlapping_area = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            overlapping_area += overlap_area(position_list[i], position_list[j])
    print(100 * n - overlapping_area)

if __name__ == '__main__':
    main()