from sys import stdin
from heapq import heappush, heappop

def main():
    stdin = open('Problem\BOJ_19638_센티와 마법의 뿅망치\input.txt', 'r')
    num_of_giants, centi_height, count_limit = map(int, stdin.readline().split(' '))
    
    pq = []
    for _ in range(num_of_giants):
        heappush(pq, -int(stdin.readline()))
        
    count = 0
    for _ in range(count_limit):
        cur_height = abs(heappop(pq))
        
        if cur_height < centi_height:
            heappush(pq, -cur_height)
            break
        elif cur_height == 1:
            heappush(pq, -cur_height)
        else:
            after_hit_height = cur_height // 2
            heappush(pq, -after_hit_height)
            count += 1
            
    max_height = abs(heappop(pq))
    if max_height < centi_height:
        print('YES')
        print(count)
    else:
        print('NO')
        print(max_height)
        
        
if __name__ == '__main__':
    main()        