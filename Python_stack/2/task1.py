"""
User enters the triangle sides and gets its surface and perimeter.
There are accessed float and int values at the user input 
"""

class Triangle:
    """
    Docstring for Triangle
    """
    def __init__(self, sides:list[float]):
        self.sides:list[float] = sides

    def get_perimeter(self):
        """
        Docstring for get_perimeter
        
        :param self: return the perimeter of the triangle
        """
        return sum(self.sides)

    def get_surface(self):
        """
        Docstring for get_surface
        
        :param self: return the surface of the triangle
        """
        half_perimeter = self.get_perimeter() / 2
        return (half_perimeter *
                               (half_perimeter - self.sides[0]) *
                               (half_perimeter - self.sides[1]) *
                               (half_perimeter - self.sides[2])) ** (1/2)
    def __str__(self):
        trianle_perimeter = self.get_perimeter()
        triangle_surface = self.get_surface()
        return str({"triangle_sides":self.sides,
                "triangle_perimeter": trianle_perimeter,
                "triangle_surface": triangle_surface})

user_triangle:list[float] = list(
    map(
    float, input("Enter three sides of the triangle with whitespaces\n").split()
    )
    )

print(Triangle(user_triangle))
