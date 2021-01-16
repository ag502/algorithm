from sys import stdin


def main():
    stdin = open('./input.txt', 'r')

    line_size = 0
    answer = ""
    for line in stdin.readlines():
        for word in line.strip().split():
            if word == "<br>":
                answer += '\n'
                line_size = 0
                continue
            if word == "<hr>":
                if line_size != 0:
                    answer += '\n'
                answer += f"{'-' * 80}\n"
                line_size = 0
                continue

            if line_size + len(word) > 80:
                answer += "\n"
                line_size = 0

            answer += f"{word} "
            line_size += len(word) + 1

    for line in answer.split("\n"):
        print(line.strip())


if __name__ == '__main__':
    main()