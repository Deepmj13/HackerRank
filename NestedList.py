# n=int(input())
# for _ in range(n+1):
#     name = input()
#     score = float(input())
        
# student = []
        
# for i in range(n):
#     student.append([name,score])

# print(student

# n = [3,4,5,2,4,5,6]
# n.reverse()
# print(n)
 
# list = [['d',1],['j',2]]

# print(sorted([x for y,x in list],reverse=True))


# student = []
# ss = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     student.append([name,score])
#     ss.append(score)
        
# sm=sorted(set(ss))
    
# smt = sorted(student,key=lambda x : x[0])
# for i,x in smt:
#     if x == h:
                
#         print(i)



# str ="Hello world"

# print(str[1:-5])

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