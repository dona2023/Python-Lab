from graphics import rectangle,circle
from graphics.threedgraphics import cuboid,sphere
l=int(input("enter the length of rect:"))
b=int(input("enter the breath of rect:"))
rectangle.rect(l,b)
r=int(input("enter the radius of circle:"))
circle.circle(r)
l1=int(input("enter the length of cuboid:"))
b1=int(input("enter the breath of cuboid:"))
h1=int(input("enter the height of cuboid:"))
cuboid.cuboid(l1,b1,h1)
r1=int(input("enter the radius of sphere:"))
sphere.sphere(r1)
