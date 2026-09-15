rows=int(input("Enter number of rows: "))
if rows<=0: print("Enter a positive number")
else:
    for row in range(1,rows+1): print("* "*row)
