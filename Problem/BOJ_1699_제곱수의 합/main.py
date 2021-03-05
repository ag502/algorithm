from sys import stdin, maxsize


def main():
    stdin = open("Problem/BOJ_1699_제곱수의 합/input.txt", "r")
    target_number = int(stdin.readline())
    
    dp = [maxsize] * (target_number + 1)

    cur_num = 1
    while True:
        cur_mul_num = cur_num ** 2
        if cur_mul_num > target_number:
            break
        
        dp[cur_mul_num] = min(dp[cur_mul_num], 1)
        
        for next_num in range(cur_mul_num + 1, target_number + 1):
            dp[next_num] = min(dp[next_num - cur_mul_num] + 1, dp[next_num])
            
        cur_num += 1
    
    print(dp[target_number])
    
if __name__ == "__main__":
    main()