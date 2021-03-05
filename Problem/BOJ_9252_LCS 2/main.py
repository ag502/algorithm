from sys import stdin
from collections import deque


def dp_reverse(row, col):
      cur_row = row
      cur_col = col
            
      string = deque()
      
      while 0 <= cur_row and 0 <= cur_col:
            cur_value = dp[cur_row][cur_col]
            
            if dp[cur_row][cur_col - 1] == cur_value:
                  cur_col -= 1
            elif dp[cur_row - 1][cur_col] == cur_value:
                  cur_row -= 1
            else:
                  string.appendleft(string1[cur_col - 1])
                  cur_row -= 1
                  cur_col -= 1
                  
      return ''.join(string)


def main():
  stdin = open("Problem/BOJ_9252_LCS 2/input.txt", "r")
  global string1, string2, dp
  string1 = stdin.readline().rstrip()
  string2 = stdin.readline().rstrip()
  
  dp = [[0] * (len(string1) + 1) for _ in range(len(string2) + 1)]
  
  for row in range(1, len(string2) + 1):
        for col in range(1, len(string1) + 1):
              if string2[row - 1] == string1[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
              else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
  
  print(dp[len(string2)][len(string1)])      
  print(dp_reverse(len(string2), len(string1)))
  

if __name__ == "__main__":
  main()