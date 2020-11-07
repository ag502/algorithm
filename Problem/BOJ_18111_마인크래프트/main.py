from sys import stdin
from collections import Counter

def main():
    stdin = open('./test_case.txt', 'r')
    rows, cols, blocks = map(int, stdin.readline().split())
    mine_map = []
    # 맵 구성
    for _ in range(rows):
        mine_map.append(list(map(int, stdin.readline().split())))

    heights = set()
    height_counter = []
    for row in range(rows):
        for col in range(cols):
            height_counter.append(mine_map[row][col])
            heights.add(mine_map[row][col])

    heights_counter = Counter(height_counter)

    time_per_height = {}
    for target_height in heights:
        needed_blocks = blocks
        time = 0
        print(target_height, sorted(heights_counter.items(), key=lambda x: (x[0] - 1000)))
        for height, count in sorted(heights_counter.items(), key=lambda x: target_height <= x[0]):
            if height < target_height:
                if needed_blocks < (target_height - height) * count:
                    break
                else:
                    needed_blocks -= (target_height - height) * count
                    time +=  (target_height - height) * count
            elif height > target_height:
                needed_blocks += (height - target_height) * count
                time += 2 * (height - target_height) * count
        else:
            time_per_height[target_height] = time

    time_per_height = sorted(time_per_height.items(), key=lambda x: (x[1], -x[0]))
    print(str(time_per_height[0][1]) + " " + str(time_per_height[0][0]))

if __name__ == '__main__':
    main()