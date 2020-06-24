from sys import stdin

def is_res_msg(message):
    alphabet_list = {}
    next_to_appear = ''

    for char in message:
        if next_to_appear != '':
            if next_to_appear != char:
                return False
            else:
                next_to_appear = ''
                continue

        if char not in alphabet_list:
            alphabet_list[char] = 1
        else:
            alphabet_list[char] += 1
            if alphabet_list[char] == 3:
                next_to_appear = char
                alphabet_list[char] = 0

    if next_to_appear != '':
        return False
    else:
        return True


def main():
    n = int(stdin.readline())

    for _ in range(n):
        message = stdin.readline().rstrip()
        if is_res_msg(message):
            print('OK')
        else:
            print('FAKE')

if __name__ == "__main__":
    main()