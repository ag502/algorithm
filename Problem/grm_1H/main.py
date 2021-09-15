from sys import stdin, maxsize

def main():
    stdin = open('Problem\grm_1H\input.txt', 'r')
    num_of_data = int(stdin.readline())
    data = list(map(int, stdin.readline().split()))

    average_value = sum(data) / num_of_data

    number_distance = maxsize
    target_data = maxsize
    target_idx = 1

    for idx, value in enumerate(data):
        if number_distance > abs(average_value - value):
            number_distance = abs(average_value - value)
            target_data = value
            target_idx = idx + 1

    print('{} {}'.format(target_idx, target_data))

if __name__ == "__main__":
    main()