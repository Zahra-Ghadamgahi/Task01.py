side1 = float(input("Enter side1:"))
side2 = float(input("Enter side2:"))
side3 = float(input("Enter side3:"))
if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
    print("these numbers can form a triangle")
else: 
    print("these numbers cant form a triangle")