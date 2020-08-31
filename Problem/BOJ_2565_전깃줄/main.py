from sys import stdin


def main():
    N = int(stdin.readline().rstrip())
    end_poll_list = [0] * 501
    cache = [1] * 501

    max_value = 0
    for _ in range(N):
        start_poll, end_poll = map(int, stdin.readline().split())
        if max_value < end_poll:
            max_value = end_poll

        end_poll_list[start_poll] = end_poll

    for i in range(2, len(end_poll_list)):
        if end_poll_list[i] == 0:
            continue
        for j in range(1, i):
            if end_poll_list[j] == 0:
                continue
            if end_poll_list[i] > end_poll_list[j]:
                cache[i] = max(cache[i], cache[j] + 1)

    print(N - max(cache[:max_value + 1]))


if __name__ == "__main__":
    main()
