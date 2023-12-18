from math import pi
while True:
      print("1.Area of circle")
      print("2.Area of rectangle")
      print("3.circumference of circle")
      print("4.Area of square")
      ch=int(input("enter ypur choice 1,2,3,4(enter 0 to exit):"))

      if ch==1:
            r=float(input("enter the radius of the circle:"))
            print("the area of the circle is ",str(pi*r**2))
      elif ch==2:
            l=int(input("enter the length of the rectangle:"))
            b=int(input("enter the breadth of the rectangle:"))
            print("the area of the rectangle is",str(l*b))
      elif ch==3:
             r=float(input("enter the radius of the circle:"))
             print("circumference of circle is ",str(2*pi*r))
      elif ch==4:
              a=int(input("enter the length of a side of square:"))
              print("Area of square is:",str(a*a))

      elif ch==0:
              break
      else:
         print("Invalid choice")

