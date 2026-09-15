items=["tv","mobile","tablet","headphones","laptop"]
cart=[]
while True:
    print("\n1 Add  2 Remove  3 Search  4 Update  5 Sort  6 Display  7 Exit")
    choice=input("Choice: ")
    if choice=="1":
        item=input("Item: ").lower()
        if item in items: cart.append(item); print("Added")
        else: print("Not available")
    elif choice=="2":
        item=input("Remove: ").lower()
        if item in cart: cart.remove(item); print("Removed")
        else: print("Not found")
    elif choice=="3":
        item=input("Search: ").lower()
        print("Found at position",cart.index(item)+1 if item in cart else "not found")
    elif choice=="4":
        old=input("Old item: ").lower(); new=input("New item: ").lower()
        if old in cart and new in items: cart[cart.index(old)]=new; print("Updated")
        else: print("Update failed")
    elif choice=="5": cart.sort(); print("Sorted")
    elif choice=="6": print("Cart:",cart)
    elif choice=="7": break
    else: print("Invalid choice")
