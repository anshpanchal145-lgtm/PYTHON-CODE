n=int(input("Enter a number: "))
if n<=0: print("Enter a positive number")
else:
    for i in range(1,11): print(f"{n} x {i} = {n*i}")
