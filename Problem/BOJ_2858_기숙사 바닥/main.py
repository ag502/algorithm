from sys import stdin

def main():
    r, b = map(int, stdin.readline().split())
    sum_of_inner_rec = r - 4
    for i in range(1, b + 1):
        if b % i == 0:
            width = b // i
            height = i
            if width >= height and (width * 2 + height * 2 == sum_of_inner_rec):
                print('{} {}'.format(width + 2, height + 2))
                return

if __name__ == "__main__":
    main()
