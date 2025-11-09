vowels = "aeiouAEIOU"
count = 0
usedvowel = []
s = input("input a String")


for ch in vowels:
    if ch in s:
        count+=1
        usedvowel.append(ch)
    
print("Total Vowels No :",count)
print("Used Vowels",usedvowel)