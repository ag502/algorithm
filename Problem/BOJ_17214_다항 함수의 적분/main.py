from sys import stdin

def main():
    stdin = open('./test_case.txt', 'r')
    polynomial = stdin.readline().rstrip()

    degrees = [0, 0]
    temp = ''
    for char in polynomial:
        if char == 'x':
            if temp == '':
                temp = '1'
            degrees[0] = int(temp)
            temp = ''
            continue
        temp += char
    if temp != "":
        degrees[1] = int(temp)

    answer = []
    for idx, coefficient in enumerate(degrees):
        if idx == 0 and coefficient != 0:
            if coefficient // 2 == 1:
                answer.append('xx')
            elif coefficient // 2 == -1:
                answer.append('-xx')
            else:
                answer.append(str(coefficient // 2) + 'xx')
        elif idx == 1 and coefficient != 0:
            if coefficient == 1:
                answer.append("+x")
            elif coefficient == -1:
                answer.append("-x")
            else:
                answer.append((str(coefficient) if coefficient < 0 else "+" + str(coefficient)) + 'x')

    answer.append('+W')

    print(''.join(answer).strip("+"))

if __name__ == '__main__':
    main()
