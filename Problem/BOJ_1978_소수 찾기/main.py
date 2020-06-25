from sys import stdin

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(stdin.readline())
    number_list = list(map(int, stdin.readline().split()))

    number_of_prime = 0
    for number in number_list:
        if is_prime(number):
            number_of_prime += 1

    print(number_of_prime)

if __name__ == '__main__':
    main()