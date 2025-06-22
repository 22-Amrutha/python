print("name:amrutha;usn:1AY24AI007;SECTION:M")

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

def distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return math.sqrt(dx*dx + dy*dy)

def point_in_circle(circle, point):
    return distance(circle.center, point) <= circle.radius

def rect_in_circle(circle, rect):
    p1 = rect.corner
    p2 = Point(p1.x + rect.width, p1.y)
    p3 = Point(p1.x, p1.y + rect.height)
    p4 = Point(p1.x + rect.width, p1.y + rect.height)
    return (point_in_circle(circle, p1) and point_in_circle(circle, p2) and
            point_in_circle(circle, p3) and point_in_circle(circle, p4))

def rect_circle_overlap(circle, rect):
    p1 = rect.corner
    p2 = Point(p1.x + rect.width, p1.y)
    p3 = Point(p1.x, p1.y + rect.height)
    p4 = Point(p1.x + rect.width, p1.y + rect.height)
    return (point_in_circle(circle, p1) or point_in_circle(circle, p2) or
            point_in_circle(circle, p3) or point_in_circle(circle, p4))
circle=Circle(Point(150,100),75)
rect = Rectangle(Point(120,80),30,40)

print("Point in Circle:", point_in_circle(circle, Point(160, 100)))
print("Rectangle in Circle:", rect_in_circle(circle, rect))
print("Rectangle Overlaps Circle:", rect_circle_overlap(circle,rect))