from sys import stdin


def main():
    n, my_score, max_length = list(map(int, stdin.readline().split()))

    rank = 1

    if n == 0:
        print(rank)
        return
    else:
        rank_score = list(map(int, stdin.readline().split()))

        for score in rank_score:
            if my_score > score:
                print(rank)
                return
            elif my_score < score:
                rank += 1

        if n == max_length and my_score <= rank_score[max_length - 1]:
            print(-1)
            return
        else:
            print(rank)


if __name__ == "__main__":
    main()