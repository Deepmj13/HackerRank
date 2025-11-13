grades = [73,69,38,33]



for i in range(len(grades)):
    count = 0
    temp = grades[i]
    while True:
        if temp % 5 != 0 :
            temp+=1
            count+=1
        else:
            if count <= 2 and grades[i]+count > 39 :
                grades[i]+=count
            break
                

print(grades)