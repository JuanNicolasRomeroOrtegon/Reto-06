from .point import Point
from .line import Line 

class Shape:
    def __init__(self, is_regular: bool, vertices: list["Point"], 
                 edges: list["Line"], inner_angles: list[float]) -> None:
        
        if (not isinstance(is_regular, bool) or not isinstance(vertices, list) 
        or not isinstance(edges, list)) or not isinstance(inner_angles, list):
            raise TypeError("You must validate the type of data entered.")

        for element in vertices:
            if not isinstance(element, Point):
                raise TypeError("The elements in vertices must be Points.")
    
        for element in edges:
            if not isinstance(element, Line):
                raise TypeError("The elements in edges must be Lines.")

        for element in inner_angles:
            if not isinstance(element, float):
                raise TypeError("The elements in inner_angles must be floats")
            
        if not vertices or not edges or not inner_angles:
            raise ValueError("The lists of data cannot be empty")
        
        if len(vertices) != len(inner_angles):
            raise ValueError("Number of vertices must match number of inner angles.") 
        #Any shape must have the same vertices and angles

        if len(vertices) < 3:
            raise ValueError("A shape must have at least 3 vertices.")
        if len(edges) < 3:
            raise ValueError("A shape must have at least 3 edges.")

        if is_regular == True:
            first_angle = inner_angles[0]
            for angle in inner_angles:
                if first_angle != angle:
                    raise ValueError("You are working with a regular Shape, so" \
                    "all of their angles must be equal.")
                
            first_length = edges[0].get_length()
            for edge in edges:
                if first_length != edge:
                    raise ValueError("You are working with a regular Shape, so" \
                    "all of their edges must be equal")


        self._is_regular = is_regular         
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles
        
    def get_is_regular(self) -> bool:
        return self._is_regular
    
    def set_is_regular(self, is_regular: bool) -> None:
        if not isinstance(is_regular, bool):
            raise TypeError("is_regular must be a boolean.")
        self._is_regular = is_regular
        
    def get_vertices(self):
        return self._vertices
    
    def set_vertices(self, vertices: list["Point"]):
        if not isinstance(vertices, list):
            raise TypeError("vertices must be a list.")
        if not vertices:
            raise ValueError("vertices list cannot be empty.")
        for vertex in vertices:
            if not isinstance(vertex, Point):
                raise TypeError("Each element in vertices must be a Point.")
        self._vertices = vertices

    def get_edges(self):
        return self._edges
    
    def set_edges(self, edges: list["Line"]):
        if not isinstance(edges, list):
            raise TypeError("edges must be a list.")
        if not edges:
            raise ValueError("edges list cannot be empty.")
        for edge in edges:
            if not isinstance(edge, Line):
                raise TypeError("Each element in edges must be a Line.")
        self._edges = edges

    def get_inner_angles(self):
        return self._inner_angles
    
    def set_inner_angles(self, inner_angles: list[float]):
        if not isinstance(inner_angles, list):
            raise TypeError("inner_angles must be a list.")
        if not inner_angles:
            raise ValueError("inner_angles list cannot be empty.")
        for angle in inner_angles:
            if not isinstance(angle, float):
                raise TypeError("Each element in inner_angles must be a float.")
        self._inner_angles = inner_angles
    

    def compute_area(self): 
        pass #El área se calcula según la figura 

    def compute_perimeter(self):
        if len(self._edges) == 0: 
            raise ValueError("The Shape doesn't have edges")
        perimeter = 0
        for edge in self._edges:
            perimeter += edge.get_length()
        return perimeter

    def compute_inner_angles(self):
        if len(self._inner_angles) == 0:
            raise ValueError("The Shape doesn't have angles")
        total_angles = 0
        for angle in self._inner_angles: 
            total_angles += angle
        return total_angles
