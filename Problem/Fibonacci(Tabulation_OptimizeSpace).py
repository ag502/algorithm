def fib_optimized(n):
    current = 1
    previous = 1

    if n < 3 & n > 0:
        return current
    for i in range(3, n + 1):
        temp = current
        current = current + previous
        previous = temp

    return current


print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
