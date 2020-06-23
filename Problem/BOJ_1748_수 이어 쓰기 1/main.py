from sys import stdin

def main():
    n = int(stdin.readline())
    length = len(str(n))

    number_of_digit = 0
    for i in range(1, length + 1):
        if i == length:
            number_of_digit += (n - 10 ** (i - 1) + 1) * i
            break
        number_of_digit += (10 ** i - 10 ** (i - 1)) * i

    print(number_of_digit)

if __name__ == "__main__":
    main()
