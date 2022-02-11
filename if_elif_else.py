#if_elif_else 
print("Enter 3 numbers:")
A = int(input("First Number = "))
B = int(input("Second Number = "))
C = int(input("Third Number = "))

if ((A>B) and (A>C)):
  print("The Largest number is ", A)
  
elif ((B>A) and (B>C)):
  print("The Largest number is ", B)

else:
  print("The Largest number is ", C)