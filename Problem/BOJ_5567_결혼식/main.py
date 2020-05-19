from sys import stdin

def main():
    n = int(stdin.readline())
    len_friend_list = int(stdin.readline())
    friend_list = {}

    for _ in range(len_friend_list):
        a, b = map(int, stdin.readline().split())
        if a in friend_list:
            friend_list[a].append(b)
        else:
            friend_list[a] = []
            friend_list[a].append(b)

        if b in friend_list:
            friend_list[b].append(a)
        else:
            friend_list[b] = []
            friend_list[b].append(a)

    invitable_friend = []
    for friend in friend_list[1]:
        invitable_friend.append(friend)
        for friend_friend in friend_list[friend]:
            invitable_friend.append(friend_friend)

    invitable_friend = set(invitable_friend)
    print(len(invitable_friend) - 1)

if __name__ == "__main__":
    main()

