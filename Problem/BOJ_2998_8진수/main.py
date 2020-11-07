from sys import stdin

convert_table = {
        '000': '0',
        '001': '1',
        '010': '2',
        '011': '3',
        '100': '4',
        '101': '5',
        '110': '6',
        '111': '7'
    }

def main():
    stdin = open('./test_case.txt', 'r')
    binary_num = stdin.readline().rstrip()

    while len(binary_num) % 3 != 0:
        binary_num = '0' + binary_num

    answer = []
    temp = []
    for idx, digit in enumerate(binary_num):
        if idx > 0 and idx % 3 == 0:
            answer.append(convert_table[''.join(temp)])
            temp = []
        temp.append(digit)
    if len(temp) != 0:
        answer.append(convert_table[''.join(temp)])

    print(''.join(answer))

if __name__ == '__main__':
    main()