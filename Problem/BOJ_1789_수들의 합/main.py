from sys import stdin

def main():
    n = int(stdin.readline())
    number_list = set()

    i = 1
    while True:
        temp = n - i
        if i < temp:
            number_list.add(i)
            n = temp
            i += 1
        else:
            number_list.add(n)
            break

    print(len(number_list))

if __name__ == "__main__":
    main()
