value=input("Enter a number: ")
if value.isdigit():
    print("Palindrome" if value==value[::-1] else "Not palindrome")
else: print("Enter a valid number")
