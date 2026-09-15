n=int(input("Enter a number: "))
reversed_num=int(str(abs(n))[::-1])
if n<0: reversed_num=-reversed_num
print("Reverse:",reversed_num)
