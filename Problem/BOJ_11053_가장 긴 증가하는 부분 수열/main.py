from sys import stdin

def main():
    n = int(stdin.readline())
    array = list(map(int, stdin.readline().split()))

    sub_array_len = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if array[i] > array[j]:
                length = sub_array_len[j] + 1
                if length > sub_array_len[i]:
                    sub_array_len[i] = length
    print(max(sub_array_len))

if __name__ == "__main__":
    main()