from re import compile


def main():
    stdin = open('./input.txt', 'r')
    num_of_chromosomes = int(stdin.readline())

    pattern = compile('^[A-F]?A+F+C+[A-F]?$')

    for _ in range(num_of_chromosomes):
        chromosome = stdin.readline().strip()

        result = pattern.match(chromosome)

        if result is None:
            print('Good')
        else:
            print('Infected!')


if __name__ == '__main__':
    main()