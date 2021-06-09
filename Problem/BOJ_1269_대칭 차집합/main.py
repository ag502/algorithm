from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    num_of_a, num_of_b = map(int, stdin.readline().split())
    set_a = set(map(int, stdin.readline().split()))
    set_b = set(map(int, stdin.readline().split()))

    a_b_intersection = set_a & set_b
    print(len(set_a) - len(a_b_intersection) + len(set_b) - len(a_b_intersection))


if __name__ == '__main__':
    main()