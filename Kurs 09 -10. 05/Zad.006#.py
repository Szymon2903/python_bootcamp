

 # Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora swobodnego dla dwuwymiarowej płaszczyźnie.
 # Wektory powinny mieć możliwość dodawania, odejmowania, mnożenia (przez liczbę),porównania  (po długości)
 # oraz powinny posiadać czytelną reprezentacje napisową.

 # Przykład użycia:

 # >>> vector_1 = Vector(x=1, y=2)
 # >>> vector_2 = Vector(x=1, y=2)
 # >>> vector_3 = vector_1 + vector_2

class Vector:

    def __init__(self):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<vector: x={self.x}, y={self.y}>"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstace(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise NotImplementedError()

class TestEvector:

    def test_init(self):
        vector = Vector(1, 2)
        assert vector.x == 1
        assert vector.y == 2

    def test_add_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = v1 + v2
        assert v3.x == 4
        assert v4.y == 6

    def test_mul_two_vectors(self):
        v1 = Vectors(1, 2)
        v2 = vectors(3, 4)
        assert vs * vs == 1 * 3 * 2 * 4

    def test_mul_vector_int(self):
        v1 = Vector(3, 4)
        v2 = v1 * 3
        assert v2.x == 9
        assert v2.y == 12

    def test_vector_comparision(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        v3 = Vector(1, 2)
        assert v2 > v1
        assert v1 < v2
        assert v1 == v3
        assert v1 != v2

    def test_length(self):
        v1 = Vector(2, 2)
        assert v1