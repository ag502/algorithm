from sys import stdin

def is_similar(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        change_table = {}
        changed_char = set()
        for char1, char2 in zip(string1, string2):
            if char1 in change_table:
                if char2 != change_table[char1]:
                    return False
            else:
                if char2 in changed_char:
                    return False
                change_table[char1] = char2
                changed_char.add(char2)
        return True

def main():
    n = int(stdin.readline())
    string_list = [stdin.readline().rstrip() for _ in range(n)]

    answer = 0
    for i in range(len(string_list) - 1):
        for j in range(i + 1, len(string_list)):
            if is_similar(string_list[i], string_list[j]):
                answer += 1

    print(answer)

if __name__ == '__main__':
    main()