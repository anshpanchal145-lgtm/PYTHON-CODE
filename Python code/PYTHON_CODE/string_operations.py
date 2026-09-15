text=input("Enter a string: ")
while True:
    print("\n1 Length  2 Upper  3 Lower  4 Capitalize  5 Split  6 Exit")
    option=input("Choice: ")
    if option=="1": print(len(text))
    elif option=="2": print(text.upper())
    elif option=="3": print(text.lower())
    elif option=="4": print(text.capitalize())
    elif option=="5": print(text.split())
    elif option=="6": break
    else: print("Invalid choice")
