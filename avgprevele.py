list =[100,200,40,70,800,520,70]

temp = list[0]
innerlist = []
for i in range(1,len(list)):
    con = temp / i
    if con < list[i] and con != list[i]:
        innerlist.append(list[i])
        temp += list[i]
    else:
        temp += list[i]


print(len(innerlist))