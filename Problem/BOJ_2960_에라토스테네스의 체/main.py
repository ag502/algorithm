from sys import stdin

def main():
    n, k = map(int, stdin.readline().split())
    number_list = [i for i in range(2, n + 1)]

    delete_count = 0
    for i in range(len(number_list)):
        if number_list[i] == -1:
            continue
        smallest_number = number_list[i]
        for j in range(i, len(number_list)):
            if number_list[j] != -1 and number_list[j] % smallest_number == 0:
                delete_count += 1
                if delete_count == k:
                    print(number_list[j])
                    return
                number_list[j] = -1

if __name__ == "__main__":
    main()

