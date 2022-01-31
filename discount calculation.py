#discount
number = int(input("Enter the price: "))
if number>1000:
  discount=number*0.05
  newprice =number-discount
  print("Discount: ", discount)
  print("New Price: ", newprice)
else:
  print("No Discount")