numbers=[4,5,1,2,34,6,7,8,45,32]
unique=sorted(set(numbers))
if len(unique)>=2:
    print("Second maximum:",unique[-2])
    print("Second minimum:",unique[1])
else: print("Need at least two distinct values")
