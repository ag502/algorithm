from sys import stdin


def main():
    stdin = open("./input.txt", "r")
    test_case = int(stdin.readline())

    for _ in range(test_case):
        string = stdin.readline().rstrip()
        k = int(stdin.readline())

        shortest_string = ''
        longest_string = ''
        for window_size in range(1, len(string) + 1):
            char_dict = {}
            flag = False
            for i in range(window_size):
                if string[i] not in char_dict:
                    char_dict[string[i]] = 1
                else:
                    char_dict[string[i]] += 1
                    if char_dict[string[i]] == k:
                        flag = True
                    else:
                        flag = False
            if flag:
                if shortest_string == '':
                    shortest_string = string[0:window_size]
                elif len(shortest_string) > len(string[0:window_size]):
                    shortest_string = string[0:window_size]

                if string[0] == string[window_size - 1]:
                    if longest_string == '':
                        longest_string = string[0:window_size]
                    elif len(longest_string) < len(string[0:window_size]):
                        longest_string = string[0:window_size]

            start = 0
            end = window_size - 1
            while True:
                left_char = string[start]
                start += 1
                end += 1
                if end >= len(string):
                    break
                next_right_char = string[end]
                char_dict[left_char] -= 1

                if next_right_char in char_dict:
                    char_dict[next_right_char] += 1
                else:
                    char_dict[next_right_char] = 1

                if char_dict[left_char] == k or char_dict[next_right_char] == k:
                    if shortest_string == '':
                        shortest_string = string[start:end + 1]
                    elif len(shortest_string) > len(string[start:end + 1]):
                        shortest_string = string[start:end + 1]
                    if string[start] == string[end]:
                        if longest_string == '':
                            longest_string = string[start:end + 1]
                        elif len(longest_string) < len(string[start:end + 1]):
                            longest_string = string[start:end + 1]
                # print(shortest_string)
                # print(longest_string)
        print(shortest_string)
        print(longest_string)

        if shortest_string == '' and longest_string == '':
            print(-1)
        else:
            print(len(shortest_string), len(longest_string))


if __name__ == '__main__':
    main()