from sys import stdin

def main():
    n = int(stdin.readline())

    five_kg = n // 5
    five_kg_remain = n % 5

    if five_kg_remain == 0:
        print(five_kg)
        return
    elif five_kg_remain % 3 == 0:
        three_kg = five_kg_remain // 3
        print(five_kg + three_kg)
        return
    else:
        for i in range(five_kg - 1, -1, -1):
            new_five_kg = n - (5 * i)
            if new_five_kg % 3 == 0:
                new_three_kg = new_five_kg // 3
                print(i + new_three_kg)
                return

    print(-1)

"""
    def main():
        n = int(stdin.readline())
        
        five = n // 5
        three = 0
        n = n % 5
        
        while five >= 0:
            if n % 3 == 0:
                three = n // 3
                n = n % 3
                break
            five -= 1
            n += 5
        print((five + three) if n == 0 else -1)
"""
if __name__ == "__main__":
    main()