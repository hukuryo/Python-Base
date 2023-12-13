# #!/usr/bin/env python

# import math


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @property
#     def distance(self):
#         return math.sqrt(self.x * self.x + self.y * self.y)
    
#     @property
#     def x(self):
#         return self._x      # getter

#     @x.setter
#     def x(self, value):
#         self._x = value

# # class Rectangle:
# #     def __init__(self, width, height):
# #         self.width = width
# #         self.height = height

# #     def area(self):
# #         return self.width * self.height
    
# # class Square(Rectangle):
# #     def __init__(self, size):
# #         super().__init__(size, size)


# # class A:
# #     def __init__(self):
# #         pass

# #     def greet(self):
# #         print('This is class A')


# # class B:
# #     def __init__(self):
# #         pass

# #     def greet(self):
# #         print('This is class B')


# # def call(x):
# #     x.greet()


# def main():
#     point = Point(10, 20)
#     print(point.x, point.y)     # _x, _y の参照は可能
#     point.x = 30
#     print(point.x)

# if __name__ == '__main__':
#     main()
