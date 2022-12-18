class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return (2*(self.length+self.breadth))
l=int(input("Enter the Length:"))
b=int(input("Enter the Breadth:"))
o=rectangle(l,b)
x=o.area()
y=o.perimeter()
print("The Area is =",x)
print("The Perimeter =",y)
l1=int(input("Enter the Length:"))
b1=int(input("Enter the Breadth:"))
o1=rectangle(l1,b1)
p=o1.area()
q=o1.perimeter()
print("The Area is:",p)
print("The Perimeter is",q)
if(x>p):
    print("The first rectangle is greater")
else:
    print("the second rectangle is greater than the first")
