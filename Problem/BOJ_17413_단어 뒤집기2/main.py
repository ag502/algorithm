from sys import stdin

def main():
    string = stdin.readline().rstrip()

    string_chunk = []
    temp = []
    is_tag = False
    for char in string:
        if char == "<":
            if len(temp) != 0:
                string_chunk.append(temp)
                temp = []
            is_tag = True
            temp.append(char)
        elif char == ">":
            temp.append(char)
            string_chunk.append(temp)
            temp = []
            is_tag = False
        elif char == " ":
            if is_tag:
                temp.append(char)
            elif not is_tag:
                if len(temp) != 0:
                    string_chunk.append(temp)
                    temp = []
                string_chunk.append(char)
        else:
            temp.append(char)
    if len(temp) != 0:
        string_chunk.append(temp)

    answer = []
    for chunk in string_chunk:
        if chunk == ' ':
            answer.append(chunk)
        elif chunk[0] == "<":
            answer.append(''.join(chunk))
        else:
            answer.append(''.join(reversed(chunk)))

    print(''.join(answer))

if __name__ == '__main__':
    main()