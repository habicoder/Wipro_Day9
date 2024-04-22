# fact.py
# fact.py

class factorial:
    def fact(self, n):
        if n == 0:
            return 1
        else:
            return n * self.fact(n - 1)

