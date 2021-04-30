from sys import stdin

vowels = {
    'z': (0, 0),
    'x': (1, 0),
    'c': (2, 0),
    'v': (3, 0),
    'a': (0, 1),
    's': (1, 1),
    'd': (2, 1),
    'f': (3, 1),
    'g': (4, 1),
    'q': (0, 2),
    'w': (1, 2),
    'e': (2, 2),
    'r': (3, 2),
    't': (4, 2)
}

consonants = {
    'b': (4, 0),
    'n': (5, 0),
    'm': (6, 0),
    'h': (5, 1),
    'j': (6, 1),
    'k': (7, 1),
    'l': (8, 1),
    'y': (5, 2),
    'u': (6, 2),
    'i': (7, 2),
    'o': (8, 2),
    'p': (9, 2)
}


def main():
    stdin = open("./input.txt")
    sl, sr = stdin.readline().split()
    string = stdin.readline().rstrip()

    sl_pos, sr_pos = [vowels[sl], consonants[sr]]

    time = 0

    for char in string:
        if sl == char or sr == char:
            time += 1
        else:
            if char in vowels:
                time += abs(vowels[char][0] - sl_pos[0]) + abs(vowels[char][1] - sl_pos[1]) + 1
                sl_pos = vowels[char]
                sl = char
            else:
                time += abs(consonants[char][0] - sr_pos[0]) + abs(consonants[char][1] - sr_pos[1]) + 1
                sr_pos = consonants[char]
                sr = char
    print(time)


if __name__ == '__main__':
    main()