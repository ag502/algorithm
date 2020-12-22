from sys import stdin

def main():
    stdin = open('./input.txt', 'r')

    test_case = int(stdin.readline())
    for _ in range(test_case):
        a_species, b_species = map(int, stdin.readline().split())
        a_list = list(map(int, stdin.readline().split()))
        b_list = list(map(int, stdin.readline().split()))

        answer = 0
        for a in a_list:
            for b in b_list:
                if a > b:
                    answer += 1

        print(answer)

if __name__ == '__main__':
    main()