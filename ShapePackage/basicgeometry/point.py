
class Point:
    def __init__(self, x: int, y: int) -> None:

        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("You must enter integers.")

        self._x = x
        self._y = y
    
    def get_x(self) -> int:
        return self._x
    
    def set_x(self, x: int) -> None:

        if not isinstance(x, int):
             raise TypeError("You must enter integers.")
        self._x = x
    
    def get_y(self) -> int:
        return self._y
    
    def set_y(self, y: int) -> None:

        if not isinstance(y, int):
             raise TypeError("You must enter integers.")
        self._y = y
    
    def compute_distance(self, other_point: "Point") -> float: 

        if not isinstance(other_point, Point):
            raise TypeError("You must enter a Point.")


        x_distance = self._x - other_point.get_x()
        y_distance = self._y - other_point.get_y()
        return (x_distance**2 + y_distance**2)** 0.5
    
        