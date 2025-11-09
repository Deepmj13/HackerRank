x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
i = [a for a in range(x+1)]
j = [b for b in range(y+1)]
k = [c for c in range(z+1)]
    
result =[ [a,b,c] for a in i for b in j for c in z if a+b+c != n ]
print(result)
