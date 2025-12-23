
# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
from typing import List
class Sol:
    def sQ(self,nums:List[int]) -> List[int]:
        n = len(nums)
        arr = [0]*n
        l,r=0,n-1
        pos=n-1
        while l<=r:
            lsq=nums[l]**2
            rsq=nums[r]**2
            if lsq >= rsq:
                arr[pos]=lsq
                l+=1
            else:
                arr[pos]=rsq
                r-=1
            
            pos-=1

        return arr
    
if __name__=="__main__":
    s=Sol()
    nums = [-4,-1,0,3,10]
    output = s.sQ(nums=nums)
    print(output)
