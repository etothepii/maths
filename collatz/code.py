class Number:

    def __init__(self, multiplicand, denominator, remainder, ultimate_parent=None):
        self.multiplicand = int(multiplicand)
        self.denominator = int(denominator)
        self.remainder = int(remainder)
        if ultimate_parent is None:
            if self.denominator != 1:
                raise ValueError("If the ultimate_patent is not set then the denominator must be 1")
            self.ultimate_parent = multiplicand + remainder
        else:
            self.ultimate_parent = ultimate_parent

    def step(self):
        if self.multiplicand + self.remainder * self.denominator < self.ultimate_parent * self.denominator:
            return set()
        if self.multiplicand % 2 == 0 and self.remainder % 2 == 0:
            return {self.child(self.multiplicand / 2, self.denominator, self.remainder / 2)}
        elif self.multiplicand % 2 == 0:
            return {self.child(self.multiplicand * 3, self.denominator, self.remainder * 3 + 1)}
        elif self.remainder % 2 == 0:
            return {
                self.child(self.multiplicand * 3, self.denominator, self.remainder * 3 + 1),
                self.child(self.multiplicand, self.denominator * 2, self.remainder / 2)
            }
        else:
            return {
                self.child(self.multiplicand * 3, self.denominator, self.remainder * 3 + 1),
                self.child(self.multiplicand, self.denominator * 2, (self.remainder + self.multiplicand) / 2)
            }

    def child(self, multiplicand, denominator, remainder):
        return Number(multiplicand, denominator, remainder, self.ultimate_parent)

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
