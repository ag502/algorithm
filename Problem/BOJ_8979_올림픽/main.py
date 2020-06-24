from sys import stdin

def main():
    n, k = map(int, stdin.readline().split())
    medal_per_country = {}
    # lambda x: (-x[1][0], -x[1][1], -x[1][2], (-1 if x[0] < 3 else 1))

    for _ in range(n):
        num_of_medal = list(map(int, stdin.readline().split()))
        medal_per_country[num_of_medal[0]] = num_of_medal[1:]

    medal_per_country = sorted(medal_per_country.items(), key=lambda x: (-x[1][0], -x[1][1], -x[1][2], (-1 if x[0] == k else 1)))

    for idx, item in enumerate(medal_per_country):
        country, medal = item
        if country == k:
            print(idx + 1)
            break

    # print(medal_per_country)
    #
    # ranking = {}
    # current_rank = 1
    # previous_country_medal = None
    # previous_medal_sum = -1
    #
    # for item in medal_per_country:
    #     country, medal = item
    #     if len(ranking) == 0:
    #         ranking[current_rank] = []
    #         ranking[current_rank].append(country)
    #         previous_country_medal = medal
    #         previous_medal_sum = sum(medal)
    #     else:
    #         if sum(medal) != previous_medal_sum or medal != previous_country_medal:
    #             current_rank += len(ranking[current_rank])
    #             ranking[current_rank] = []
    #             ranking[current_rank].append(country)
    #             previous_country_medal = medal
    #             previous_medal_sum = sum(medal)
    #         else:
    #             ranking[current_rank].append(country)
    #
    # for rank, country_list in ranking.items():
    #     if k in country_list:
    #         print(rank)
    #         break

if __name__ == "__main__":
    main()