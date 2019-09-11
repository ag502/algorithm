def fib_memo(n, cache):
    if not bool(cache):
        cache.update({1: 1, 2: 1})
    if n in cache:
        return cache[n]
    else:
        nth_value = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
        cache.update({n: nth_value})
        return cache[n]

    # if n < 3:
    #   return 1
    # if n in cache:
    #   return cache[n]
    # cache[n] = fib(n - 1, cache) + fib(n - 2, cache)
    # return cache[n]


def fib(n):
    fib_cache = {}

    return fib_memo(n, fib_cache)


print(fib(10))
print(fib(50))
print(fib(100))