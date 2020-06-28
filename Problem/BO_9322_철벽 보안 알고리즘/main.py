from sys import stdin

def get_key(pk1, pk2):
    key = []
    for idx, word in enumerate(pk1):
        key.append((idx, pk2.index(word)))

    return key

def main():
    test_case = int(stdin.readline())

    for _ in range(test_case):
        num_of_words = int(stdin.readline())
        public_key_1 = list(stdin.readline().split())
        public_key_2 = list(stdin.readline().split())
        encryption = list(stdin.readline().split())

        keys = get_key(public_key_1, public_key_2)
        plain = [0] * len(encryption)

        for key in keys:
            plain[key[0]] = encryption[key[1]]

        print(' '.join(plain))

if __name__ == '__main__':
    main()