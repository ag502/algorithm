from sys import stdin

def main():
    test_case = int(stdin.readline())
    for _ in range(test_case):
        is_consistence = True
        num_of_phones = int(stdin.readline())
        phones = [0] * num_of_phones
        for idx in range(num_of_phones):
            phones[idx] = stdin.readline().rstrip()

        phones.sort(key=lambda x: len(x))

        phones_set = set()
        phones_set.add(phones[0])

        for phone_num in phones[1:]:
            for idx in range(0, len(phone_num)):
                if phone_num[:idx + 1] in phones_set:
                    print("NO")
                    is_consistence = False
                    break
            if not is_consistence:
                break

            phones_set.add(phone_num)
        if is_consistence:
            print("YES")

if __name__ == '__main__':
    main()