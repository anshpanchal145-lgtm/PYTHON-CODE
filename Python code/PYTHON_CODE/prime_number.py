n=int(input("Enter a number: "))
prime=n>1 and all(n%d!=0 for d in range(2,int(n**0.5)+1))
print("This is a prime number" if prime else "This is not a prime number")
