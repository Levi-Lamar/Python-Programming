#net bonus 
salary = float(input("Enter Salary: "))#user enter salary

time = int(input("Enter years of service: "))

if time>10: #check if time is less than 10 years
  bonus=salary*10/100
  print("Net bonus is ", bonus)

if time>=6 and time<=10:
  bonus=salary*8/100
  print("Net bonus is ", bonus)

else:
  bonus=salary*5/100 #check if time is less than 6 years
  print("Net bonus is ", bonus)