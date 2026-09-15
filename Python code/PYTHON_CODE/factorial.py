n=int(input("Enter a number: "))
if n<0: print("Enter a non-negative number")
else:
    result=1
    for value in range(2,n+1): result*=value
    print("Factorial:",result)
