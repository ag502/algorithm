from sys import stdin

def main():
    n = int(stdin.readline())
    enter = set()

    for _ in range(n):
        name, status = stdin.readline().split()

        if status == 'enter':
            enter.add(name)
        elif status == 'leave':
            enter.remove(name)

    enter = sorted(enter, reverse=True)

    for name in enter:
        print(name)

if __name__ == '__main__':
    main()