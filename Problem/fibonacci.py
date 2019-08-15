class Fibonacci:
    def fib(self, n):
        if n <= 2:
            return 1
        return self.fib(n - 2) + self.fib(n - 1)


fibonacci = Fibonacci()

for i in range(1, 11):
    print(fibonacci.fib(i))
