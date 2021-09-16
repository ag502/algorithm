from sys import stdin

def is_inside(x, y, r):
    distance = x ** 2 + y ** 2
    if distance < r ** 2:
        return True
    return False

def main():
    stdin = open('Problem\grm_2H\input.txt', 'r')
    test_case = int(stdin.readline())

    for idx in range(test_case):
        r = int(stdin.readline())
        
        total_pixel = 0
        prev_height = r
        for x in range(0, r):
            height = 0
            for y in range(prev_height, -1, -1):
                if is_inside(x, y, r):
                    height = y + 1
                    prev_height = height
                    break
            total_pixel += height

        print('#{}'.format(idx + 1))
        print(total_pixel * 4)

if __name__ == "__main__":
    main()