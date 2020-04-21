from sys import stdin


def main():
    num_of_student = int(stdin.readline())

    input_rank = [int(stdin.readline()) for _ in range(num_of_student)]
    input_rank = sorted(input_rank, key=lambda x: x)

    rank_sum = 0

    #0~len(arr)-1
    for i in range(len(input_rank)):
        rank_sum += abs(input_rank[i] - (i + 1))

    print(rank_sum)


if __name__ == "__main__":
    main()