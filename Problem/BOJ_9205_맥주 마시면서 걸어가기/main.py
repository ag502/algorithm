from sys import stdin

def main():
    test_case = int(stdin.readline())
    for _ in range(test_case):
        num_of_convenience = int(stdin.readline())
        home_pos = list(map(int, stdin.readline().split()))
        stores_pos = []
        for _ in range(num_of_convenience):
            stores_pos.append(list(map(int, stdin.readline().split())))
        festival_pos = list(map(int, stdin.readline().split()))
