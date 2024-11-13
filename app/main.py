import math
from typing import Tuple


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x_coordinate + other.x_coordinate,
                      self.y_coordinate + other.y_coordinate)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x_coordinate - other.x_coordinate,
                      self.y_coordinate - other.y_coordinate)

    def __mul__(self, other: any) -> any:
        if isinstance(other, (int, float)):
            return Vector(self.x_coordinate * other,
                          self.y_coordinate * other)
        elif isinstance(other, Vector):
            return round(self.x_coordinate * other.x_coordinate
                         + self.y_coordinate * other.y_coordinate, 4)
        else:
            raise ValueError("Unsupported type for multiplication")

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float],
     end_point: Tuple[float, float]
    ) -> "Vector":
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x_coordinate ** 2 + self.y_coordinate ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x_coordinate / length, self.y_coordinate / length)

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector
        lengths_product = self.get_length() * vector.get_length()
        if lengths_product == 0:
            return 0
        cos_a = dot_product / lengths_product
        cos_a = max(min(cos_a, 1), -1)
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x_coordinate * math.cos(radians) - self.y_coordinate * math.sin(radians)
        new_y = self.x_coordinate * math.sin(radians) + self.y_coordinate * math.cos(radians)
        return Vector(new_x, new_y)
