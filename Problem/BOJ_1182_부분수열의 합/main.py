from sys import stdin

stdin = open("./input.txt", "r")
length_of_array, target = map(int, stdin.readline().split())
array = list(map(int, stdin.readline().split()))
array.sort()

answer = 0


def back_tracking(cur_idx, acc):
    global answer
    acc += array[cur_idx]

    for next_idx in range(cur_idx + 1, length_of_array):
        back_tracking(next_idx, acc)
    if acc == target:
        answer += 1


def main():
    for idx in range(length_of_array):
        back_tracking(idx, 0)

    print(answer)


if __name__ == '__main__':
    main()