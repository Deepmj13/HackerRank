marks = [78, 45, 23, 90, 67, 88, 12, 36, 54, 100]

# print("Highest Marks",max(marks))
# print("Lowest Marks",min(marks))
# print("Average Marks",sum(marks)/len(marks))
# print(sorted(marks,reverse = True))
# passed = [x for x in marks if x>=40]
# print(passed)
# print(len(passed
# ))



highest = 0
for i in range(len(marks)):
    if highest < marks[i]:
        highest = marks[i]

print(highest)

lowest = marks[1]
for i in range(len(marks)):
    if lowest> marks[i]:
        lowest =marks[i]

print(lowest)

average = 0 
for x in marks:
    average += x

print(average/len(marks))

for i in range(len(marks)):
    for j in range(i+1,len(marks)):
        if marks[i] < marks[j]:
            marks[i],marks[j] = marks[j],marks[i] 

print(marks)

passed = []

for x in marks:
    if x >= 40:
        passed.append(x)

print(passed)

count = 0
for x in passed:
    count+=1

print(count)