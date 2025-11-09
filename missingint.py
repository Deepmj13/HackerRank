orderNumbers = [3, 4, -1, 0,1,3,2]

sortList = sorted(orderNumbers)
temp = 0
for i in range(len(sortList)):
    if sortList[i] == -1 or sortList[i] > -1:
        if sortList[i] == temp:
            temp += 1
    
print(temp)
        
