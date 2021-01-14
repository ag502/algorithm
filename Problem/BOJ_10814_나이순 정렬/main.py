from sys import stdin


def main():
    stdin = open('./input.txt', 'r')
    num_of_members = int(stdin.readline())

    members = []
    for idx in range(num_of_members):
        member_info = stdin.readline().split()
        members.append([idx] + [int(member_info[0])] + [member_info[1]])

    members = sorted(members, key=lambda x: (x[1], x[0]))

    for _, age, name in members:
        print(str(age) + " " + name)


if __name__ == '__main__':
    main()