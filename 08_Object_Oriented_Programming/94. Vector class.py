# Problem statement
# Create a Vector class that represents a two-dimensional vector using two coordinates: x and y.
#
# Your class must support vector addition, vector subtraction, equality comparisons, and scalar multiplication by overloading Python's special methods.
# Requirements
# Your Vector class must:
# 1. Accept two coordinates (x and y) when creating a vector.
# 2. Implement __add__ to add two vectors.
# 3. Implement __sub__ to subtract one vector from another.
# 4. Implement __eq__ to check whether two vectors are equal.
# 5. Implement __mul__ to multiply a vector by a scalar (integer or floating-point number).
# 6. Implement __repr__ to provide a readable representation of a vector.

class Vector:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __repr__(self):
        return f'Vector({self.X},{self.Y})'

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        else:
            return Vector(self.X + other.X, self.Y + other.Y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        else:
            return Vector(self.X - other.X, self.Y - other.Y)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        else:
            return (self.X == other.X) and (self.Y == other.Y)

    def __mul__(self, other):
        if isinstance(other, (int, float)) and not isinstance(other, bool):
            return Vector(self.X * other, self.Y * other)
        else:
            return NotImplemented

v1 = Vector(3, 4)
v2 = Vector(2, 5)

print(v1 + v2)

print(v1 - v2)

print(v1 == v2)

print(v1 * 3)

print(v1 == Vector(3, 4))
