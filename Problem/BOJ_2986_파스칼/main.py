from sys import stdin
import math

def main():
    n = int(stdin.readline())
    counter = 0

    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            counter = n - (n // i)
            break
    if counter == 0:
        counter = n - 1
    print(counter)

if __name__ == "__main__":
    main()