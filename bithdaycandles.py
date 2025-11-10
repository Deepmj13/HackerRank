l = [1,2,3,5,5]

rs = sorted(l,reverse=True)
temp = 0
for i in rs:
    if rs[0] == i:
        temp+=1

print(temp)