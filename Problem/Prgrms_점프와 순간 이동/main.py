def solution(n):
    ans = 0

    result = n
    while result != 0:
        if result % 2 == 1:
            ans += 1
        result = result // 2

    return ans

print(solution(5000))
