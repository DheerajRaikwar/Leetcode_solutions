def threeSum(nums):
    i=0
    ar = []
    for j in range(2,len(nums)):
        if nums[i]+nums[j-1]+nums[j]==0:
            ar.append([nums[i],nums[j-1],nums[j]])
        return ar
            

ar=[-1,0,1,2,-1,-4]
print(threeSum(ar))
                      
        
