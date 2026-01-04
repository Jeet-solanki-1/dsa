
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
class Sol():
    def square_of_sorted_array(self,nums:list[int])-> list[int]:
        result=[0]*len(nums)
        l,r=0,len(nums)-1
        pos=len(nums)-1
        while l<=r:
            l_sq=nums[l]**2
            r_sq=nums[r]**2
            if l_sq<=r_sq:
                result[pos]=r_sq
                r-=1
            else:
                result[pos]=l_sq
                l+=1
            
            pos-=1
        
        return result

if __name__=="__main__":
    s=Sol()
    nums = [-4,-1,0,3,10]
    out=s.square_of_sorted_array(nums=nums)
    print(out)

