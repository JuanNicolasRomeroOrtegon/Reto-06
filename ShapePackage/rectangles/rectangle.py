from ..basicgeometry.shape import Shape   

class Rectangle(Shape):
    def __init__(self, vertices: list, edges: list) -> None:

        if len(edges) != 4:
            raise ValueError("A rectangle must have 4 edges")

        if len(vertices) != 4:
            raise ValueError("A rectangle must have 4 vertices")

        angles = [90.0, 90.0, 90.0, 90.0]
        super().__init__(is_regular=False, vertices=vertices, edges=edges, inner_angles=angles)
        self._width = edges[0].get_length()
        self._height = edges[1].get_length()
            
    def get_width(self) -> float:
        return self._width
    
    def set_width(self, width: float) -> None:
        if not isinstance(width, (int, float)):
            raise TypeError("You must enter a float or a integer.")
        if width <= 0:
            raise ValueError("The width must be positive")
        self._width = width
    
    def get_height(self) -> float:
        return self._height
    
    def set_height(self, height: float) -> None:
        if not isinstance(height, (int, float)):
            raise TypeError("You must enter a float or a integer.")
        if height <= 0:
            raise ValueError("The height must be positive")
        self._height = height
    
    def compute_area(self):
        return self._width * self._height

    def compute_perimeter(self):
        return 2 * (self._width + self._height)
    
    def compute_angles(self):
        return 360
    
    def diagonal_length(self) -> float:
        return (self._width**2 + self._height**2) **0.5
    