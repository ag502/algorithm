from sys import stdin

def find(parents, country):
    # 루트일 경우
    if country == parents[country]:
        return country
    parents[country] = find(parents, parents[country])
    return parents[country]

def alliance(parents, rank, powers, country1, country2):
    country1_root = find(parents, country1)
    country2_root = find(parents, country2)

    if rank[country2_root] > rank[country1_root]:
        temp = rank[country1_root]
        rank[country1_root] = rank[country2_root]
        rank[country2_root] = temp

    parents[country2_root] = country1_root
    powers[country1_root] += + powers[country2]

    if rank[country1_root] == rank[country2_root]:
        rank[country1_root] += 1

def fight(parents, ranks, powers, country1, country2):
    country1_root = find(parents, country1)
    country2_root = find(parents, country2)

    if powers[country1_root] > powers[country2_root]:
        parents[country2_root] = country1_root
        powers[country1_root] -= powers[country2_root]
        if ranks[country2_root] > ranks[country1_root]:
            ranks[country2_root] += ranks[country1_root]

        if ranks[country1_root] == ranks[country2_root]:
            ranks[country1_root] += 1
    elif powers[country1_root] < powers[country2_root]:
        parents[country1_root] = country2_root
        powers[country2_root] -= powers[country1_root]
        if ranks[country2_root] < ranks[country1_root]:
            ranks[country1_root] += ranks[country2_root]

        if ranks[country1_root] == ranks[country2_root]:
            ranks[country2_root] += 1
    else:
        powers[country1_root] = powers[country2_root] = 0


def main():
    stdin = open('./test_case.txt', 'r')
    countries, records = map(int, stdin.readline().split())
    powers = [0] * (countries + 1)

    for i in range(1, countries + 1):
        powers[i] = int(stdin.readline())

    # 1. 초기화
    parents = [i for i in range(countries + 1)]
    ranks = [0] * (countries + 1)

    for _ in range(records):
        o, p, q = map(int, stdin.readline().split())
        if o == 1:
            alliance(parents, ranks, powers, p, q)
        else:
            fight(parents, ranks, powers, p, q)

    answer_country = set()
    answer_power = []
    for country in parents[1:]:
        answer_country.add(find(parents, country))

    for country in answer_country:
        answer_power.append(powers[country])
    answer_power.sort()

    print(len(answer_country))
    print(' '.join(map(str, answer_power)))

if __name__ == '__main__':
    main()