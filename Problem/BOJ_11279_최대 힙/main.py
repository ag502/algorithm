from sys import stdin
from heapq import heappush, heappop

def main():
    stdin = open("Problem/BOJ_11279_최대 힙/input.txt")
    n = int(stdin.readline())
    
    heap = []
    for _ in range(n):
        x = int(stdin.readline())
        if x == 0:
            if not heap:
                print(0)
            else:
                print(-heappop(heap))
        else:
            heappush(heap, -x)
            

if __name__ == "__main__":
    main()