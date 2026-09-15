watch = []

def add():
    wid = int(input("Enter Watch ID  "))
    wname = input("Enter Watch Name  ")
    brand = input("Enter Brand  ")
    price = int(input("Enter Watch Price  "))
    wtype = input("Enter Type (Analog/Digital/Smart)  ")
    color = input("Enter Color  ")

    d1 = {
        "ID": wid,
        "Name": wname,
        "Brand": brand,
        "Price": price,
        "Type": wtype,
        "Color": color
    }
    watch.append(d1)


def display():
    print("\n==============================================================")
    print("                     WATCH COLLECTION")
    print("==============================================================")
    print("ID   Name             Brand       Price      Type       Color")
    print("--------------------------------------------------------------")

    for w1 in watch:
        print(w1["ID"], "  ",
              w1["Name"], "        ",
              w1["Brand"], "     ",
              w1["Price"], "      ",
              w1["Type"], "     ",
              w1["Color"])

    print("==============================================================")


def search():
    wid = int(input("Enter Watch ID  "))
    found = 0

    for w1 in watch:
        if w1["ID"] == wid:
            found = 1
            break

    if found == 1:
        print("\n*** Watch is found ***")
        print("--------------------------------------------------------------")
        print("ID   Name             Brand       Price      Type       Color")
        print("--------------------------------------------------------------")
        print(w1["ID"], "  ",
              w1["Name"], "        ",
              w1["Brand"], "     ",
              w1["Price"], "      ",
              w1["Type"], "     ",
              w1["Color"])
        print("--------------------------------------------------------------")
    else:
        print("Watch not found")


def updateName():
    wid = int(input("Enter Watch ID whose name you want to change  "))
    found = 0

    for w1 in watch:
        if w1["ID"] == wid:
            found = 1
            break

    if found == 1:
        print("*** Watch is found ***")
        wname = input("Enter New Watch Name  ")
        w1["Name"] = wname

        print("\n*** Updated Watch ***")
        print("--------------------------------------------------------------")
        print("ID   Name             Brand       Price      Type       Color")
        print("--------------------------------------------------------------")
        print(w1["ID"], "  ",
              w1["Name"], "        ",
              w1["Brand"], "     ",
              w1["Price"], "      ",
              w1["Type"], "     ",
              w1["Color"])
        print("--------------------------------------------------------------")
    else:
        print("Watch not found")


def deletebyID():
    wid = int(input("Enter Watch ID which you want to delete  "))
    found = 0

    for w1 in watch:
        if w1["ID"] == wid:
            watch.remove(w1)
            found = 1
            print("Watch is deleted successfully")
            break

    if found == 0:
        print("Watch not found")


def sortByPrice():
    if not watch:
        print("No watches available to sort.")
        return

    watch.sort(key=lambda x: x["Price"])
    print("Watches sorted by price successfully!")
    display()
