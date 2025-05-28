from .triangle import Triangle

class Scalene(Triangle): 
    def __init__(self, vertices: list, edges: list, inner_angles
                 : list[float]) -> None:
        super().__init__(is_regular = False, vertices = vertices, edges = edges
                         , inner_angles = inner_angles)
        
        self.side1 = edges[0].get_length()
        self.side2 = edges[1].get_length()
        self.side3 = edges[2].get_length()

        if(edges[0].get_length() == edges[1].get_length() or edges[0].get_length() 
           == edges[2].get_length() or edges[1].get_length() == edges[2].get_length()): 
            raise ValueError("All the sides must be different")

    #Usamos la fórmula de Herón para calcular el área, ya que es aplicable a 
    #cualquier triángulo
    def compute_area(self):
        #sp es el semiperímetro, lo coloqué así para que no ocupase tanto espacio
        sp = (self.get_side1() + self.get_side2() + self.get_side3()) / 2
        return (sp * (sp - self.get_side1()) * (sp - self.get_side2()) * 
                (sp - self.get_side3())) ** 0.5
    
