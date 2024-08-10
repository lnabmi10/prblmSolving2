val=3
nums=[0,1,2,5,6,8,3,4,3,6]
k=0

if len(nums)>0:
        
    max_nums=max(nums)

    for i in range(0,len(nums)) :
        if nums[i] == val :
           nums[i]=max_nums+1
        else :
            k+=1

nums.sort()

print(k)
print(nums)

        
