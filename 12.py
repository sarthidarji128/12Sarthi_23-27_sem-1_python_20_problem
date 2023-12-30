class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def genNumber(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

n = int(input("Enter an number: "))
obj = DivisibleBySeven(n).genNumber()

for num in obj:
    print(num)
