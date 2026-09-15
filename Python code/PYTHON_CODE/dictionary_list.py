records=[]
count=int(input("How many students? "))
for _ in range(max(0,count)):
    records.append({"name":input("Name: "),"age":int(input("Age: ")),"course":input("Course: ")})
print("--- Student Database ---")
for no,person in enumerate(records,1):
    print(no, person["name"], person["age"], person["course"])
