def prime_check(n):
    if n<2: return False
    for divisor in range(2,int(n**0.5)+1):
        if n%divisor==0: return False
    return True

n=int(input("Enter a number: "))
print("Prime number" if prime_check(n) else "Not a prime number")
