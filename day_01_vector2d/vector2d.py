import math 
class Vector2D:
    def __init__(self,a,b):
        self.a = a 
        self.b = b 

    def __repr__(self):
        return f"Vector2D({self.a},{self.b})"    

    def __add__(self,other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.a + other.a, self.b + other.b)
    
    def __sub__(self,other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.a - other.a, self.b - other.b)
    
    def __mul__(self,other):
        if isinstance(other, (int,float)):
            return Vector2D(self.a * other, self.b * other)
        if isinstance(other, Vector2D):
            return Vector2D(self.a * other.a, self.b * other.b)
        return NotImplemented
    
    def __eq__(self,other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.a == other.a and self.b == other.b 
    
    def __abs__(self):
        return math.sqrt(self.a**2 + self.b**2)
