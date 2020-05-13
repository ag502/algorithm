from sys import stdin

def main():
    n = int(stdin.readline())
    cache = [0] * 1000001

    cache[1] = 1
    cache[2] = 2

    for index in range(3, n + 1):
        cache[index] = (cache[index - 1] + cache[index - 2]) % 15746

    print(cache[n])

if __name__ == "__main__":
    main()