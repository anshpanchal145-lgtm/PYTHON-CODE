for row in range(1,6):
    spaces="  "*(5-row)
    numbers=" ".join(str(x) for x in range(5,5-row,-1))
    print(spaces+numbers)
