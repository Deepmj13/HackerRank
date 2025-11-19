

def checkstring(string):
    characters = "abcdefghijklmnopqrstuvwxyz"
    check = []
    for i in string.lower():
        if i in characters:
            check.append(i)
    
    return check == check[::-1]




string = input("Enter String")

if checkstring(string):
    print("palindrome")
else:
    print("not palindrome")
