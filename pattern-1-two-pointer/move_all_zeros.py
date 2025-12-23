# 283. Move Zeroes

# Given an integer array nums, move all 0's to
#  the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 
# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
from typing import List
class Sol:
    def movZ(self,nums:List[int]) ->None:
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1
        
        for i in range(slow,len(nums)):
            nums[i]=0
        
        print(nums)
        

if __name__=="__main__":
    s=Sol()
    nums = [1]
    s.movZ(nums=nums)
