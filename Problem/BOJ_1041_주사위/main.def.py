from sys import stdin

def main():
    n = int(stdin.readline())
    dice_num = list(map(int, stdin.readline().split()))

    if n == 1:
        print(sum(sorted(dice_num)[0:5]))
    else:
        three_min_num = [min(dice_num[0], dice_num[5]),
                         min(dice_num[1], dice_num[4]),
                         min(dice_num[2], dice_num[3])]
        three_min_num.sort()

        num_of_one = (n - 2) ** 2 + ((n - 2) * (n - 1) * 4)
        num_of_two = 4 * (n - 2) +  4 * (n - 1)
        num_of_three = 4

        print(three_min_num[0] * num_of_one
              + (three_min_num[0] + three_min_num[1]) * num_of_two
              + (three_min_num[0] + three_min_num[1] + three_min_num[2]) * num_of_three
              )

if __name__ == "__main__":
    main()