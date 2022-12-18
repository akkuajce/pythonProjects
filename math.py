import Graphics.circle
import Graphics.rectangle
import Graphics.GraphicsThreeD.cuboid
import Graphics.GraphicsThreeD.sphere

print("Area of circle:",Graphics.circle.area(2))
print("Perimeter of circle:",Graphics.circle.perimeter(3))

print("Area of rectangle:",Graphics.rectangle.area(2,3))
print("Perimeter of rectanglr:",Graphics.rectangle.perimeter(3,3))

print("Area of cuboid:",Graphics.GraphicsThreeD.cuboid.area(1,1,1))
print("Perimeter of cuboid:",Graphics.GraphicsThreeD.cuboid.perimeter(1,1,1))

print("Area of sphere:",Graphics.GraphicsThreeD.sphere.area(3))
print("Perimeter of sphere:",Graphics.GraphicsThreeD.sphere.perimeter(2))
