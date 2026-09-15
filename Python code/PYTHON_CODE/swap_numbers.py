a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Before: A={a}, B={b}")
a,b=b,a
print(f"After: A={a}, B={b}")
