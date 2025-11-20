def ffo(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


nums = int(input("Enter no"))
target = int(input("enter target"))

code = ffo(nums,target)
print(code)