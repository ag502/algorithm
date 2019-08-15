class TriangleSum:
    def triangle_number(self, n):
        if n == 1:
            return 1
        return self.triangle_number(n - 1) + n


for i in range(1, 11):
    print(TriangleSum().triangle_number(i))
