num=int(input("Enter a number: "))
original=num
power=len(str(abs(num)))
total=0
for digit in str(abs(num)):
    total += int(digit) ** power
print("Armstrong number" if total==abs(original) else "Not an Armstrong number")
