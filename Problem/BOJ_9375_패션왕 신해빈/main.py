from sys import stdin
from itertools import combinations

def main():
    test_case = int(stdin.readline())
    for _ in range(test_case):
        num_of_clothes = int(stdin.readline())
        clothes_list = {}
        for _ in range(num_of_clothes):
            cloth_name, cloth_category = list(stdin.readline().split())
            if cloth_category not in clothes_list:
                clothes_list[cloth_category] = []
            clothes_list[cloth_category].append(cloth_name)

        num_of_case = 1
        for key in clothes_list:
            num_of_case *= (len(clothes_list[key]) + 1)
        print(num_of_case - 1)

if __name__ == '__main__':
    main()

