name = input("Enter your name: ")
family = input("Enter your family: ")
a = float(input("Enter your score in mathematics: "))
b = float(input("Enter your score in literature: "))
c = float(input("Enter your score in sport: "))
avg = a+b+c/3
if avg>=17:
   print("status : Great")
elif avg>=12:
   print("status : Normal")
else:
   print("status : failed")