from sys import stdin

def main():
    room_number = stdin.readline().rstrip()
    number_set = {}

    for number in room_number:
        if number == '9' or number == '6':
            if '9' not in number_set and '6' not in number_set:
                number_set[number] = 1
            elif '6' not in number_set:
                number_set['6'] = 1
            elif '9' not in number_set:
                number_set['9'] = 1
            else:
                if number_set['9'] < number_set['6']:
                    number_set['9'] += 1
                else:
                    number_set['6'] += 1
        else:
            if number in number_set:
                number_set[number] += 1
            else:
                number_set[number] = 1

    number_set = sorted(number_set.items(), key=lambda x: -x[1])
    print(number_set[0][1])

if __name__ == '__main__':
    main()