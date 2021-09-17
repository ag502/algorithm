from sys import stdin

# def is_continuous_seq(array, length):
#     for idx in range(length - 1):
#         if array[idx] != array[idx + 1] - 1:
#             return False
#     return True

# def main():
#     stdin = open('Problem\grm_2I\input.txt', 'r')
#     num_of_episodes = int(stdin.readline())
#     episodes = list(map(int, stdin.readline().split()))

#     episodes.sort()
    
#     print('YES' if is_continuous_seq(episodes, num_of_episodes) else 'NO')

# if __name__ == "__main__":
#     main()

def main():
    stdin = open('Problem\grm_2I\input.txt', 'r')
    num_of_episodes = int(stdin.readline())
    episodes = list(map(int, stdin.readline().split()))
    
    max_episode, min_episode = max(episodes), min(episodes)
    
    kind_of_episode = max_episode- min_episode + 1
    if kind_of_episode == num_of_episodes:
        print('YES')
    else:
        print('NO')
    
if __name__ == "__main__":
    main()