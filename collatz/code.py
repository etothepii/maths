class Number:

    def __init__(self, multiplicand, denominator, remainder):
        self.multiplicand = multiplicand
        self.denominator = denominator
        self.remainder = remainder

    def step(self):
        pass

    def __repr__(self):
        if self.denominator == 1:
            return f"{self.multiplicand} * n + {self.remainder}"
        return f"({self.multiplicand} * n) / {self.denominator} + {self.remainder}"
