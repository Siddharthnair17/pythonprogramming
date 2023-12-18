class Rectangle:
  def __init__(self):
      self.l=float(input("enter length"))
      self.b=float(input("enter breath"))
  def area(self):
      self.ar=self.l*self.b
      print("Area=",self.ar)
  def perim(self):
      self.per=2*(self.l+self.b)
      print("perimeter=",self.per)
print("Rectangle1:")
r1=Rectangle();
r1.area()
r1.perim()
print("Rectangle2:")
r2=Rectangle();
r2.area()
r2.perim()
if(r1.ar>r2.ar):
   print("Rectangle has greater area")
elif(r1.ar==r2.ar):
   print("Rectangle have equal area")
else:
   print("Rectangle has greater area")



