# Here x is a new reference to same list lst
def myFun(x):
    x[3] = 50
 
 
# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)