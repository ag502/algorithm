from sys import stdin
from collections import deque

def is_same_seq(seq1, seq2):
    seq1_list = list(seq1)
    seq2_list = list(seq2)

    if len(seq1_list) != len(seq2_list):
        return False

    if seq1_list == seq2_list:
        return True
    else:
        return False

def main():
    n = int(stdin.readline())
    seq_of_book = deque()
    original_of_book = deque()
    for i in range(1, n + 1):
        seq_of_book.append(int(stdin.readline()))
        original_of_book.append(i)

    top_seq = deque()
    top_seq.append(seq_of_book[0])

    move_count = 0
    while True:
        next_top = top_seq[0] - 1

        if next_top == 1:
            top_seq.appendleft(next_top)
            move_count += 1
            if is_same_seq(top_seq, original_of_book):
                print(move_count)
                break
        elif next_top <= 0:
            if len(top_seq) == n - 1:
                top_seq.append(n)
                if is_same_seq(top_seq, original_of_book):
                    print(move_count)
                    break
                else:
                    top_seq.appendleft(top_seq.pop())
                    move_count += 1
        else:
            top_seq.appendleft(next_top)
            move_count += 1

        if len(top_seq) == n:
            top_seq.pop()

if __name__ == "__main__":
    main()