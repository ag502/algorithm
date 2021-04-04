from sys import stdin
from heapq import heappush, heappop

def main():
    stdin = open("Problem/BOJ_1927_최소 힙/input.txt")
    n = int(stdin.readline())
    
    heap = []
    for _ in range(n):
        x = int(stdin.readline())
        if x == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heappop(heap))
        else:
            heappush(heap, x)
        
if __name__ == "__main__":
    main()