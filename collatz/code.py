class Number:

    def __init__(self, multiplicand, denominator, remainder):
        self.multiplicand = int(multiplicand)
        self.denominator = int(denominator)
        self.remainder = int(remainder)

    def step(self):
        if self.multiplicand % 2 == 0 and self.remainder % 2 == 0:
            return {Number(self.multiplicand / 2, self.denominator, self.remainder / 2)}
        pass

    def __repr__(self):
        if self.denominator == 1:
            return f"{self.multiplicand} * n + {self.remainder}"
        return f"({self.multiplicand} * n) / {self.denominator} + {self.remainder}"

    def __hash__(self):
        return self.multiplicand + self.remainder

    def __eq__(self, other):
        if isinstance(other, Number):
            return other.multiplicand == self.multiplicand and \
                   other.denominator == self.denominator and \
                   other.remainder == self.remainder
