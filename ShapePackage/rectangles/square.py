from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, vertices: list, edges: list) -> None:
        super().__init__(vertices, edges)
        
        side = edges[0].get_length()
        for element in edges:
            if side  != element.get_length():
                raise ValueError("The sides of a square must be equal.")
        self._side = side

    def get_side(self) -> float:
        return self._side

    def set_side(self, side: float) -> None:
        if not isinstance(side, (int, float)):
            raise TypeError("Side must be a number.")
        if side <= 0:
            raise ValueError("The side must be positive")
        self._side = side

    def compute_area(self) -> float:
        return self._side**2

    def compute_perimeter(self) -> float:
        return 4 * self._side

    def compute_angles(self) -> float:
        return 360
