class ConsecutiveSum:
    def consecutive_sum(self, start, end):
        # 1 ~ 1, 2 ~ 2
        if start == end:
            return start
        # 1 ~ 8 => 1 ~ 4 5 ~ 8
        # 1 ~ 9 => 1 ~ 4 5 ~ 9
        return self.consecutive_sum(start, (start + end) // 2) \
            + self.consecutive_sum((start + end) // 2 + 1, end)


print(ConsecutiveSum().consecutive_sum(1, 10))
print(ConsecutiveSum().consecutive_sum(1, 100))
print(ConsecutiveSum().consecutive_sum(1, 253))
print(ConsecutiveSum().consecutive_sum(1, 388))
