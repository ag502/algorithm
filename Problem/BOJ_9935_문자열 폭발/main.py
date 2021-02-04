from sys import stdin
from re import compile, sub


def main():
    stdin = open("./input.txt", "r")
    origin_string = stdin.readline().rstrip()
    string_bomb = stdin.readline().rstrip()

    regex = compile(string_bomb)

    prev_string = ""
    while True:
        if prev_string == origin_string:
            break
        prev_string = origin_string
        origin_string = sub(regex, "", origin_string)

    if origin_string == "":
        print("FRULA")
    else:
        print(origin_string)


if __name__ == '__main__':
    main()