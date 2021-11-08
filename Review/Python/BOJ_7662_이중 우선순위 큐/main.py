from sys import stdin
from heapq import heappush, heappop

def main():
    stdin = open('Review\Python\BOJ_7662_이중 우선순위 큐\input.txt', 'r')
    
    test_case = int(stdin.readline())
    
    for _ in range(test_case):
        max_heap = []
        min_heap = []
        max_heap_delete = {}
        min_heap_delete = {}
        
        num_of_commands = int(stdin.readline())
        
        for command in range(num_of_commands):
            command, number = stdin.readline().split(" ")

            if command == 'I':
                heappush(min_heap, int(number))
                heappush(max_heap, -int(number))
            elif command == 'D':
                delete_type = int(number)
                if delete_type == -1:
                    while min_heap:
                        cur_value = min_heap[0]
                        
                        if cur_value not in max_heap_delete or max_heap_delete[cur_value] == 0:
                            break
                        max_heap_delete[cur_value] -= 1
                        heappop(min_heap)
                    
                    if min_heap:
                        cur_value = heappop(min_heap)
                        if cur_value in min_heap_delete:
                            min_heap_delete[cur_value] += 1
                        else:
                            min_heap_delete[cur_value] = 1
                        
                elif delete_type == 1:
                    while max_heap:
                        cur_value = -max_heap[0]
                        
                        if cur_value not in min_heap_delete or min_heap_delete[cur_value] == 0:
                            break
                        min_heap_delete[cur_value] -= 1
                        heappop(max_heap)
                        
                    if max_heap:
                        cur_value = -heappop(max_heap)
                        if cur_value in max_heap_delete:
                            max_heap_delete[cur_value] += 1
                        else:
                            max_heap_delete[cur_value] = 1
        
        while max_heap:
            cur_max_value = -max_heap[0]
            if cur_max_value not in min_heap_delete or min_heap_delete[cur_max_value] == 0:
                break
            heappop(max_heap)
            min_heap_delete[cur_max_value] -= 1
            
        while min_heap:
            cur_min_value = min_heap[0]
            if cur_min_value not in max_heap_delete or max_heap_delete[cur_min_value] == 0:
                break
            heappop(min_heap)
            max_heap_delete[cur_min_value] -= 1
            
            
        if not min_heap or not max_heap:
            print('EMPTY')
        else:
            print('%s %s' % (-heappop(max_heap), heappop(min_heap)))

if __name__ == "__main__":
    main()