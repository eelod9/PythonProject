nums= [2,7,11,15]
target = 9
f = {}
for i, num in enumerate(nums):
    if num not in f:
        f[target-num]= i
        print(f"Update{f}")
    else:
        f[num] , i
        print(f"{f[num]}")
        print(i)
        