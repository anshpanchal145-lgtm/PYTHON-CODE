value=int(input("Enter a number: "))
even=odd=0
for digit in str(abs(value)):
    if int(digit)%2==0: even+=1
    else: odd+=1
print("Number:",value)
print("Even digits:",even)
print("Odd digits:",odd)
