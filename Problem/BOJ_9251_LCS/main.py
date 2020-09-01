from sys import stdin


def main():
    S1 = stdin.readline().rstrip()
    S2 = stdin.readline().rstrip()

    S1_list = list(S1)
    S2_list = list(S2)

    cache = [0] * len(S2_list)

    prev_alphabet = ''

    for i in range(len(S1_list)):
        target_alphabet = S1_list[i]
        max_length = 0
        is_in = False
        for j in range(len(S2_list)):
            if S2_list[j] == prev_alphabet:
                if max_length < cache[j]:
                    max_length = cache[j]
            if S2_list[j] == target_alphabet:
                is_in = True
                cache[j] = max(cache[j], max_length + 1)
                # max_length = 0
        if is_in:
            prev_alphabet = target_alphabet

    # print(max(cache))
    print(cache)


if __name__ == "__main__":
    main()
