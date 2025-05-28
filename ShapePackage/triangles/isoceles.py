
from .triangle import Triangle

class Isoceles(Triangle):
    def __init__(self, vertices: list, edges: list, 
                 inner_angles: list[float]) -> None:
        super().__init__(is_regular=False, vertices=vertices, edges=edges, 
                         inner_angles=inner_angles)
        

        sides = [self.get_side1(), self.get_side2(), self.get_side3()]
        unique_sides = set(sides)
        if len(unique_sides) != 2:
            raise ValueError("An isosceles triangle must have two equal sides exactly.")
         
    def equal_sides(self) -> float:
        side1 = self.get_side1()
        side2 = self.get_side2()
        side3 = self.get_side3()
        if side1 == side2 or side1 == side3:
            return side1
        else:
            return side2

    def compute_area(self) -> float:
        side1 = self.get_side1()
        side2 = self.get_side2()
        side3 = self.get_side3()

        if side1 == side2:
            equal_side = side1
            base = side3
        elif side1 == side3:
            equal_side = side1
            base = side2
        else:
            equal_side = side2
            base = side1

        return (base / 4) * ((4 * equal_side**2 - base**2) ** 0.5)