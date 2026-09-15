import CrudOp_watch as c1

while True:
    print("\n****************************************")
    print("          WATCH MANAGEMENT SYSTEM")
    print("****************************************")
    print("1. Add Watch")
    print("2. Display Watches")
    print("3. Update Watch Name")
    print("4. Delete Watch")
    print("5. Search Watch")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    print("----------------------------------------")

    if choice == "1":
        c1.add()

    elif choice == "2":
        c1.display()

    elif choice == "3":
        c1.updateName()

    elif choice == "4":
        c1.deletebyID()

    elif choice == "5":
        c1.search()

    elif choice == "6":
        print("Exiting application. Goodbye!")
        break

    else:
        print("Invalid option selected. Please choose between 1 and 6.")
