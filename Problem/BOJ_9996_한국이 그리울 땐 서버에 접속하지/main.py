from sys import stdin

def main():
    num_of_words = int(stdin.readline())
    pattern = stdin.readline().rstrip()
    front, back = pattern.split('*')

    for _ in range(num_of_words):
        word = stdin.readline().rstrip()

        if len(word) < len(front) + len(back):
            print("NE")
            continue

        if word[0:len(front)] == front and word[len(word) - len(back):] == back:
            print("DA")
        else:
            print("NE")

if __name__ == '__main__':
    main()