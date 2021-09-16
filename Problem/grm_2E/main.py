from sys import stdin

def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

def main():
    stdin = open('Problem\grm_2E\input.txt', 'r')
    test_case = int(stdin.readline())

    for idx in range(test_case):
        target_number = int(stdin.readline())
        print('Case #{}'.format(idx + 1))
        print('YES' if is_prime(target_number) else 'NO')

if __name__ == "__main__":
    main()