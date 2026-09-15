rows=int(input("Enter number of rows: "))
if rows<=0: print("Enter a positive number")
else:
    for row in range(rows,0,-1):
        print("  "*(rows-row)+"* "*(2*row-1))
