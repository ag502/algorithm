from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    num_of_lines = int(stdin.readline())
    lines = []

    for _ in range(num_of_lines):
        lines.append(list(map(int, stdin.readline().split())))

    lines.sort(key=lambda x: (x[0], x[1]))
    # print(lines)

    answer = [lines[0]]

    for line in lines[1:]:
        start, end = line
        standard = answer[len(answer) - 1]

        if standard[1] < start:
            answer.append(line)
        else:
            answer[len(answer) - 1][1] = max(end, answer[len(answer) - 1][1])

    total_length = 0
    for start, end in answer:
        total_length += end - start

    print(total_length)


if __name__ == '__main__':
    main()