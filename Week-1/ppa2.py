class Triangle:
    def __inti__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def isValid(self):
        if self.a+self.b>c and self.a+self.c>self.b and self.b+self.c > self.a:
            return "Valid"
        return "Invalid"

    #classification according to the side
    def classification_Sides(self):
        if self.isValid() == "Invalid":
            return 'Invalid'
        if self.a == self.b == self.c :
            return "Equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Isosceles"
        else:
            return "Scalene"

    #classification on the bases of the angle
    def angle_classification(self):
        if self.isValid() == "Invalid":
            return 'Invalid'
        
        sides = sorted([self.a , self.b , self.c])
        x,y,z = sides

        if x*x + y*y > z*z:
            return "Acute"
        elif x*x + y*y == z*z:
            return "Right"
        else:
            return "Obtuse"

    
    # Calculate area using Heron's Formula
    def Area(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"

        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area


# Example
t = Triangle(3, 4, 5)

print(t.Is_valid())
print(t.Side_Classification())
print(t.Angle_Classification())
print(t.Area())
