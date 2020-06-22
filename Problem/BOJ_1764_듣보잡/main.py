from sys import stdin

def main():
    n, m = list(map(int, stdin.readline().split()))

    never_heard = [stdin.readline().rstrip() for _ in range(n)]
    never_seen = [stdin.readline().rstrip() for _ in range(m)]

    never_heard = set(never_heard)
    never_seen = set(never_seen)

    never_heard_seen = never_heard & never_seen
    never_heard_seen = sorted(never_heard_seen, key=lambda x: x)

    print(len(never_heard_seen))
    for name in never_heard_seen:
        print(name)

if __name__ == "__main__":
    main()