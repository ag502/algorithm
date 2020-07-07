from sys import stdin

def main():
    document = stdin.readline().rstrip()
    template = stdin.readline().rstrip()

    answer = 0
    idx = 0
    while idx <= len(document) - len(template):
        if document[idx:idx + len(template)] == template:
            answer += 1
            idx += len(template) - 1
        idx += 1

    print(answer)

if __name__ == '__main__':
    main()