student={
    "name":input("Enter name: "),
    "age":int(input("Enter age: ")),
    "course":input("Enter course: ")
}
print("--- Student Details ---")
for key,val in student.items(): print(f"{key}: {val}")
