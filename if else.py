#if else statement
username = str(input("Enter Username : "))
pwd = int(input("Enter Password : "))

logins = ["BSCIT-05-0269/2020", 123]

if ((username in logins) and (pwd in logins)):
  print("Login Successful")
else:
  print("Login Failed")