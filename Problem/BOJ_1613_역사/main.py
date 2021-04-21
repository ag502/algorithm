from sys import stdin

stdin = open("./input.txt", "r")
num_of_event, num_of_relation = map(int, stdin.readline().split())

events = [[float("INF")] * (num_of_event + 1) for _ in range(num_of_event + 1)]
for _ in range(num_of_relation):
    prev_event, next_event = map(int, stdin.readline().split())
    events[prev_event][next_event] = 1

test_case = int(stdin.readline())
test_events = []
for _ in range(test_case):
    test_events.append(list(map(int, stdin.readline().split())))


def main():
    for k in range(1, num_of_event + 1):
        for i in range(1, num_of_event + 1):
            if events[i][k] == float("INF"):
                continue
            for j in range(1, num_of_event + 1):
                events[i][j] = min(events[i][k] + events[k][j], events[i][j])

    for event1, event2 in test_events:
        if events[event1][event2] != float("INF"):
            print(-1)
        elif events[event2][event1] != float("INF"):
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    main()