from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    num_of_classes = int(stdin.readline())

    classes = []
    for _ in range(num_of_classes):
        start_time, terminate_time = map(int, stdin.readline().split())
        classes.append([start_time, terminate_time])

    classes.sort(key=lambda x: (x[1], x[0]))
    check = [0] * num_of_classes


    answer = 0
    print(classes)
    print(check)


if __name__ == '__main__':
    main()