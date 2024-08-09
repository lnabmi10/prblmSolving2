class Solution(object):
    def removeDuplicates(self, nums):
        p=len(nums)
        new_list=[nums[0]]
        largest_element = max(nums)
        for i in range(1,p):
            if nums[i] in new_list:
                 nums[i]=largest_element+1
                 
            else :
                new_list.append(nums[i])

        print(nums)
        print(new_list)    
        nums.sort()
        k=len(new_list)
        

        
        return  k
    
    x=removeDuplicates("d",[0,0,1,1,1,1,2,2,2,3,3,3,4])
    print(x)