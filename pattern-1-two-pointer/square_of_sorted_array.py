
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

class Solution:
    def square_of_sorted(self,nums:list[int]) -> list[int]:
        #so we have to make changes IN-PLACE!
        result = [0]*len(nums)
        # as the question said the array is sorted so so big values are at last but when -ve get squared they can be doubled so
        # starting index are vulnuable as -4 -> 16 and +3 will come later so
        #  the thisng is -100 and +10 so -100-> 10000 and +10 will gove 100 only so we have to insert at last 
        # so indx will point to last
        indx_of_result = len(nums)-1

        left , right = 0, len(nums)-1
        while left <= right:
            left_sq = nums[left]**2
            right_sq = nums[right]**2
            if left_sq<=right_sq:
                result[indx_of_result]= right_sq
                right-=1
            else:
                result[indx_of_result]= left_sq
                left+=1
            
            indx_of_result-=1

        
        return result

if __name__ == "__main__":
    s = Solution()
    nums = [-7,-3,2,3,11]
    # now calling to change, and hten checking output
    Output =  s.square_of_sorted(nums=nums)
    print(Output)
    
