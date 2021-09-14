from sys import stdin

TARGET_UNIVERSITY = 'AJOU'

def main():
    stdin = open('Problem\grm_1G\input.txt', 'r')
    num_of_universities = int(stdin.readline())
    
    universities = []
    for _ in range(num_of_universities):
        universities.append(stdin.readline().rstrip())

    first_idx, last_idx = 0, 0
    is_first_find = False

    for idx, university in enumerate(universities):
        if university == TARGET_UNIVERSITY:
            if not is_first_find:
                is_first_find = True
                first_idx = idx
                last_idx = idx
            else:
                last_idx = idx


    print('{} {}'.format(first_idx + 1, last_idx + 1))
        

if __name__ == "__main__":
    main() 