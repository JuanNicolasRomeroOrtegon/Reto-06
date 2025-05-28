
from .triangle import Triangle

class TriRectangle(Triangle):
    def __init__(self, vertices: list, edges: list, inner_angles: list[float]) -> None:
        super().__init__(is_regular=False, vertices=vertices, edges=edges, inner_angles=inner_angles)
        if inner_angles[0] != 90 and inner_angles[1] != 90 and inner_angles[2] != 90:
            raise ValueError("At least one angle must be 90°")


    def compute_area(self) -> float:
        sides = sorted([self.get_side1(), self.get_side2(), self.get_side3()])
        return (sides[0] * sides[1]) / 2

    def hypotenuse(self) -> float:
        return max(self.get_side1(), self.get_side2(), self.get_side3())
    