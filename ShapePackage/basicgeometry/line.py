from .point import Point
#Importamos la clase Point desde el módulo Point.py 

class Line:
    def __init__(self, start_point: Point, end_point: Point) -> None:

        if not isinstance(start_point, Point) or not isinstance(end_point, Point):
            raise TypeError("The data entered must be Points.")
        
        if start_point == end_point:
            raise ValueError("The points must be differents") 
        #The points must be differente because if they're equal we do not get a line

        self._start_point = start_point
        self._end_point = end_point
        self._length = start_point.compute_distance(end_point)
    
    def get_start_point(self) -> Point:
        return self._start_point
    
    def set_start_point(self, start_point: Point) -> None:
        if not isinstance(start_point, Point):
            raise TypeError("You must enter a Point")
        if start_point == self._end_point:
            raise ValueError("The points must be differents")


        self._start_point = start_point
        self._length = self._start_point.compute_distance(self._end_point)
    
    def get_end_point(self) -> Point:
        return self._end_point
    
    def set_end_point(self, end_point: Point) -> None:
        if not isinstance(end_point, Point):
            raise TypeError("You must enter a Point")
        if end_point == self._start_point:
            raise ValueError("The points must be differents")

        self._end_point = end_point
        self._length = self._start_point.compute_distance(self._end_point)
    
    def get_length(self) -> float:
        return self._length
    