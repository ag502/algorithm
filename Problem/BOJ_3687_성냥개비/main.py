from sys import stdin, maxsize

matches = [2, 5, 5, 4, 5, 6, 3, 7, 6, 7]


def main():
    dp = [0] * 101
    dp[2] = (1, 1)
    dp[3] = (7, 7)

    for cur_match in range(4, 101):
        min_value = maxsize
        max_value = 0
        for prev_match in range(2, (cur_match // 2) + 1):
            match1 = dp[cur_match - prev_match]
            match2 = dp[prev_match]

            min_match1 = str(match1[0])
            max_match1 = str(match1[1])
            min_match2 = str(match2[0])
            max_match2 = str(match2[1])

            if cur_match <= 7:
                for i, num_of_match in enumerate(matches):
                    if num_of_match == cur_match:
                        min_value = i + 1
                        break
            else:
                if min_match1 == '0' and min_match2 == '0':
                    continue
                if min_match1 == '0':
                    min_value = min(min_value, int(min_match2 + min_match1))
                elif min_match2 == '0':
                    min_value = min(min_value, int(min_match1 + min_match2))
                else:
                    min_value = min(min_value, int(min_match1 + min_match2), int(min_match2 + min_match1))

            max_value = max(max_value, int(max_match1 + max_match2), int(max_match2 + max_match1))

        dp[cur_match] = (min_value, max_value)

    print(dp)

    stdin = open("./input.txt", "r")
    test_case = int(stdin.readline())
    for _ in range(test_case):
        num = int(stdin.readline())
        print(dp[num][0], dp[num][1])


if __name__ == '__main__':
    main()


