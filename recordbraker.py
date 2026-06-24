scores = [3,4,21,36,10,28,35,5,24,42]

minscore = scores[0]
maxscore = scores[0]

brakes = {"maximum":0,"manimum":0}

for i in scores:
    if minscore > i :
        minscore = i
        brakes["minimum"] += 1
    elif maxscore < i:
        maxscore = i
        brakes["maximum"] += 1

print(brakes)
