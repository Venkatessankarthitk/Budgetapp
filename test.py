# class Polygon:
#     def __init__(self, no_of_sides=None):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class Triangle(Polygon):
#     def __init__(self):
#         no_of_sides = input("Enter number of sides ")
#         Polygon.__init__(self,no_of_sides)

#     def findArea(self):
#         a, b, c = self.sides
#         # calculate the semi-perimeter
#         s = (a + b + c) / 2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)


# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()
# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
    
# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()
# def smart_divide(func):
#    def inner(a,b):
#       print("I am going to divide",a,"and",b)
#       if b == 0:
#          print("Whoops! cannot divide so I'm making 0 to 1")
#          b =1 

#       return func(a,b)
#    return inner

# @smart_divide
# def divide(a,b):
#     return a/b

# abc = divide(5,0)
# print(abc)

# class Celsius:
#     def __init__(self, temperature = 0):
#         self._temperature = temperature

#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32

#     @property
#     def temperature(self):
#         print("Getting value")
#         return self._temperature

#     @temperature.setter
#     def temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         print("Setting value")
#         self._temperature = value

# c = Celsius()
# print(c.temperature)
# c.temperature = 37
# print(c.temperature)
# print(c.to_fahrenheit())

# import copy

# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)

# old_list[1][1] = 'AA'

# print("Old list:", old_list)
# print('ID of Old List:', id(old_list))
# print("New list:", new_list)
# print('ID of Old List:', id(new_list))
####assert#####
def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))