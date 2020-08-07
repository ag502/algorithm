from sys import stdin
from collections import deque


def main():
    num_of_command = int(stdin.readline())
    queue = deque()
    for _ in range(num_of_command):
        command = stdin.readline().rstrip().split()
        if command[0] == 'push':
            queue.append(int(command[1]))
        elif command[0] == 'pop':
            if not queue:
                print(-1)
            else:
                print(queue.popleft())
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            print(1 if not queue else 0)
        elif command[0] == 'front':
            print(-1 if not queue else queue[0])
        elif command[0] == 'back':
            print(-1 if not queue else queue[len(queue) - 1])


if __name__ == "__main__":
    main()
