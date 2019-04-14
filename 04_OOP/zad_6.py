class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector ({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other

    def __lt__(self, other):
        return(self.x ** 2 + self.y **2) < (other.x ** 2 + other.y **2)

    def __eq__(self, other):
        return (self.x ** 2 + self.y ** 2) == (other.x ** 2 + other.y ** 2)

    def __le__(self, other):
        return (self.x ** 2 + self.y ** 2) <= (other.x ** 2 + other.y ** 2)

if __name__ == "__main__":
    v1 = Vector(1,2)
    print(v1)

    print (Vector(1, 2) + Vector(1, 2))
    print(Vector(1, 2)* 3)
    print(3 * Vector(1, 2))
    print (Vector(1, 2) > Vector(0, 2))
    print(Vector(1, 2) == Vector(1, 2))
    print(Vector(1, 2) >= Vector(1, 2))