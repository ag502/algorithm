from sys import stdin

def main():
    stdin = open('Problem\grm_2J\input.txt', 'r')
    num_of_cups, window_size = map(int, stdin.readline().split())
    
    cups = list(map(int, stdin.readline().split()))
    
    sum_of_nums = sum(cups[:window_size])
    if (sum_of_nums % 2 == 0):
        print('YES')
        return

    for i in range(num_of_cups - window_size):
        sum_of_nums -= cups[i]
        sum_of_nums += cups[(i + window_size)]
        
        if (sum_of_nums % 2 == 0):
            print('YES')
            return
    
    print('NO')
    
if __name__ == "__main__":
    main()