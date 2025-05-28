from .triangle import Triangle

class Equilateral(Triangle):
    def __init__(self, vertices: list, edges: list) -> None:
        side = edges[0].get_length()
        angles = [60.0, 60.0, 60.0]
        super().__init__(is_regular = True, vertices = vertices, edges = edges,
                         inner_angles = angles)
        self.set_side1(side)
        self.set_side2(side)
        self.set_side3(side) 

        if (edges[0].get_length() != edges[1].get_length() or edges[0].get_length() 
        != edges[2].get_length()):
            raise ValueError("An equilateral triangle must have its sides " \
            "with the same length")

    def height(self) -> float:
        #Altura del triángulo equilátero: (√3/2) * lado
        self._height = (((3)**0.5) / 2) * self.get_side1()
        return self._height
        
    def compute_area(self):
        #Usamos la fórmula específica para triángulos equiláteros
        #Base * altura / 2
        return self.height() * self.get_side1() / 2