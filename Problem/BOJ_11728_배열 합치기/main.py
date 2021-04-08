from sys import stdin

stdin = open("./input.txt", "r")

a_len, b_len = map(int, stdin.readline().split())
array_a = list(map(int, stdin.readline().split()))
array_b = list(map(int, stdin.readline().split()))


def main():
    start_a, start_b = 0, 0
    answer = []

    while start_a < len(array_a) and start_b < len(array_b):
        cur_a_elem = array_a[start_a]
        cur_b_elem = array_b[start_b]
        if cur_a_elem < cur_b_elem:
            answer.append(cur_a_elem)
            start_a += 1
        elif cur_a_elem > cur_b_elem:
            answer.append(cur_b_elem)
            start_b += 1
        else:
            answer.append(cur_a_elem)
            answer.append(cur_b_elem)
            start_a += 1
            start_b += 1

    if start_a >= a_len and start_b < b_len:
        answer += array_b[start_b:]
    elif start_b >= b_len and start_a < a_len:
        answer += array_a[start_a:]

    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    main()

