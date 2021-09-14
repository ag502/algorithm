from sys import stdin

def main():
    stdin = open('Problem\grm_1E\input.txt', 'r')
    num_of_members, person_max_weight, machine_max_weight = map(int, stdin.readline().split())
    member_weights = list(map(int, stdin.readline().split()))

    sum_of_weight = 0
    num_of_possible_member = 0
    for weight in member_weights:
        if weight > person_max_weight:
            continue
        sum_of_weight += weight
        num_of_possible_member += 1
    
    print('{} {}'.format(num_of_possible_member, sum_of_weight))

    if sum_of_weight > machine_max_weight:
        print('NO')
    else:
        print("YES")

if __name__ == "__main__":
    main()