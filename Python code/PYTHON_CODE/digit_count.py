def digit_count(value):
    return sum(ch.isdigit() for ch in value)

text=input("Enter text: ")
print("Digits:",digit_count(text))
