import math
op = input("Enter op : + , - , / , * , sin , cos , tan , cot , factorial , radical:" )
num1 = float(input("Enter num1:"))
num2 = float(input("Enter num2:"))
if op == "+":
    result = num1 + num2
if op == "-":
    result = num1 - num2
if op == "*":
    result = num1 * num2
if op == "/":
    if num2 == 0 :
        print("Error")
    else:
        result = num1 / num2
if op == "sin":
    num = int(input("Enter num:"))
    result = math.sin(math.radians(num))
if op == "cos":
    num = int(input("Enter num:"))
    result = math.cos(math.radians(num))
if op == "tan":
    num = int(input("Eter num:"))
    result = math.tan(math.radians(num))
if op == "cot":
    num = int(input("Enter num:"))
    result = math.cot(math.radians(num))
if op == "factorial":
    num = int(input("Enter num:"))
    result = math.factorial(num)
if op == "radical":
    num = int(input("Enter num:"))
    if num >= 0:
        result = math.sqrt(num)
    else:
         print ("Error")
print (result)
    
