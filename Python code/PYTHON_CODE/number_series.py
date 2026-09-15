terms=int(input("How many Fibonacci terms? "))
a,b=0,1
for _ in range(max(0,terms)):
    print(a)
    a,b=b,a+b
