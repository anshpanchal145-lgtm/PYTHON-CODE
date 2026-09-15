text=input("Enter a string: ")
vowel_set=set("aeiouAEIOU")
count=sum(1 for ch in text if ch in vowel_set)
print("Total vowels:",count)
