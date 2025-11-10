def miniMaxSum(arr):
    sortedarr = sorted(arr)
    minsum = maxsum = 0
    for i in range(4):
        minsum+=sortedarr[i]
        n = len(arr)
        revsort = sorted(arr,reverse=True)
    for i in range(4):
        maxsum += revsort[i]
        
    print(minsum,maxsum)


arr = list(input("enter list"))
miniMaxSum(arr)