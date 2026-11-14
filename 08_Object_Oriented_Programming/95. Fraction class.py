# Problem statement
# Create a Fraction class that represents rational numbers using a numerator and denominator.
#
# Your class must automatically reduce fractions to their simplest form and support basic arithmetic operations.
#
# For example, a fraction such as \(\frac{6}{8}\) should automatically become \(\frac{3}{4}\).
# Requirements
# Your Fraction class must:
# 1. Accept a numerator and denominator when creating a fraction.
# 2. Automatically reduce the fraction to its simplest form.
# 3. Ensure the denominator is always positive.
# 4. Implement __add__ to add two fractions.
# 5. Implement __sub__ to subtract two fractions.
# 6. Implement __mul__ to multiply two fractions.
# 7. Implement __truediv__ to divide two fractions.
# 8. Implement __eq__ to compare two fractions for equality.
# 9. Implement __repr__ to display the fraction clearly.


import math


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        # Normalize the sign so the denominator is always positive
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        # Simplify the fraction
        gcd = math.gcd(numerator, denominator)

        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        n = (self.numerator * other.denominator) + \
            (self.denominator * other.numerator)
        d = self.denominator * other.denominator

        return Fraction(n, d)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        n = (self.numerator * other.denominator) - \
            (self.denominator * other.numerator)
        d = self.denominator * other.denominator

        return Fraction(n, d)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        n = self.numerator * other.numerator
        d = self.denominator * other.denominator

        return Fraction(n, d)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by a zero fraction")

        n = self.numerator * other.denominator
        d = self.denominator * other.numerator

        return Fraction(n, d)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return (self.numerator == other.numerator and
                self.denominator == other.denominator)


# Testing
f1 = Fraction(2, 4)
f2 = Fraction(1, 3)
f3 = Fraction(2, 4)

print(f1)                 # Fraction(1, 2)
print(f1 + f2)            # Fraction(5, 6)
print(f1 - f2)            # Fraction(1, 6)
print(f1 * f2)            # Fraction(1, 6)
print(f1 / f2)            # Fraction(3, 2)
print(f1 == f3)           # True

print(Fraction(6, 8))     # Fraction(3, 4)
print(Fraction(2, -4))    # Fraction(-1, 2)
print(Fraction(-2, -4))   # Fraction(1, 2)
print(Fraction(10, 15))   # Fraction(2, 3)
