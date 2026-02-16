"""
User enters the Rectangle sides and gets its surface and perimeter.
There are accessed float and int values at the user input 
"""
class NotValidRectangle(Exception):
    """
    Exception for the case user inputs not two values
    """
    def __str__(self):
        return "Please, enter two positive real values for (a, b) sides of the rectangle."

class Rectangle:
    """
    Docstring for Rectangle
    """
    def __init__(self, sides:list[float]):
        if len(sides) != 2 or sides[0] < 0 or sides[1] < 0:
           raise NotValidRectangle
        else:
            self.sides:list[float] = sides

    def get_perimeter(self):
        """
        Docstring for get_perimeter
        
        :param self: return the perimeter of the rectangle
        """
        
        return sum(self.sides) * 2

    def get_surface(self):
        """
        Docstring for get_surface
        
        :param self: return the surface of the rectangle
        """
        return self.sides[0] * self.sides[1]
    
    def __str__(self):
        rectangle_perimeter = self.get_perimeter()
        rectangle_surface = self.get_surface()
        return str({"rectangle":self.sides,
                "rectangle_perimeter": rectangle_perimeter,
                "rectangle_surface": rectangle_surface})

user_rectangle:list[float] = list(
    map(
    float, input("Enter two sides of the rectangle with whitespaces\n").split()
    )
    )

print(Rectangle(user_rectangle))
