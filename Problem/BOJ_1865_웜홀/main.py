from sys import stdin

def main():
    test_case = int(stdin.readline())
    for _ in range(test_case):
        n, m, w = map(int, stdin.readline().split())
        space = {}


        for i in range(1, n + 1):
            space[i] = []

        for _ in range(m):
            s, e, t = map(int, stdin.readline().split())
            space[s].append([e, t])
            space[e].append([s, t])

        for _ in range(w):
            s, e, t = map(int, stdin.readline().split())
            space[s].append([e, -t])

        # Bellman-Ford
        for start_planet in range(1, n + 1):
            upper = [float('inf')] * (n + 1)
            upper[start_planet] = 0
            updated = False
            for _ in range(n):
                updated = False
                for cur_planet in range(1, n + 1):
                    for next_planet, time in space[cur_planet]:
                        if upper[cur_planet] + time < upper[next_planet]:
                            upper[next_planet] = upper[cur_planet] + time
                            updated = True
                if not updated:
                    break
            if updated:
                upper = []

            if len(upper) == 0:
                print("YES")
                break
        else:
            print("NO")

if __name__ == '__main__':
    main()
