def fib_tab(n):
    nth_fib = [1, 1]
    for i in range(2, n + 1):
        nth_fib.append(nth_fib[i - 1] + nth_fib[i - 2])
    return nth_fib[n - 1]


print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))