from sys import stdin

def main():
    n = int(stdin.readline())
    participant = [int(stdin.readline()) for _ in range(n)]
    participant = sorted(participant, key=lambda x: -x)

    max_score = participant[0] + 1
    answer = 1

    for i in range(1, n):
        if max_score > participant[i] + n:
            break
        max_score = max(max_score, participant[i] + i + 1)
        answer += 1

    print(answer)

if __name__ == "__main__":
    main()