#GRADE SYSTEM
print("Enter Marks Obtained in 3 units: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())

tot = markOne+markTwo+markThree
avg = tot/3

if avg>=70 and avg<=100:
    print("avg = ", avg, "Grade is A")
elif avg>=60 and avg<=69:
    print("avg = ", avg, "Grade is C")
elif avg>=50 and avg<=59:
    print("avg = ", avg, "Grade is D")
elif avg>=40 and avg<=49:
    print("avg = ", avg, "Grade is E")
else:
    print("Invalid Input!")