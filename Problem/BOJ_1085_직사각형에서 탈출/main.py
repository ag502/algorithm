from sys import stdin

x, y, w, h = list(map(int, stdin.readline().split()))
print(min(h - y, y, w-x, x))