from sys import stdin

base = ["A", "C", "G", "T"]


def main():
    stdin = open("./input.txt", "r")
    num_of_dna, length_of_dna = map(int, stdin.readline().split())

    dna = []
    for _ in range(num_of_dna):
        dna.append(list(stdin.readline().rstrip()))

    cache = [[0] * 4 for _ in range(length_of_dna)]

    for col in range(length_of_dna):
        for row in range(num_of_dna):
            if dna[row][col] == "A":
                cache[col][0] += 1
            elif dna[row][col] == "C":
                cache[col][1] += 1
            elif dna[row][col] == "G":
                cache[col][2] += 1
            elif dna[row][col] == "T":
                cache[col][3] += 1

    answer_dna = ""
    hamming_dist = 0
    for row in range(length_of_dna):
        temp = 0
        min_base = ""
        for col in range(4):
            if temp < cache[row][col]:
                temp = cache[row][col]
                min_base = base[col]
        hamming_dist += num_of_dna - temp
        answer_dna += min_base

    print(answer_dna)
    print(hamming_dist)


if __name__ == '__main__':
    main()