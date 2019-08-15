class SumDigits:
    def sum_digits(self, n):
        if n // 10 == 0:
            return n
        return self.sum_digits(n // 10) + n % 10


print(SumDigits().sum_digits(22541))
print(SumDigits().sum_digits(92130))
print(SumDigits().sum_digits(12634))
print(SumDigits().sum_digits(704))
print(SumDigits().sum_digits(3755))
