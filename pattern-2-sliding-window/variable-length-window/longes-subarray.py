# Scenario:
#  Given an array of positive integers, find the longest sub-array whose sum is less than or equal to $S$ (a target sum).

from typing import List
class Sol:
    def longesSubarray(self,data,s):
        left=0
        current_sum=0
        max_len=0
        # we are taking snapshoot of longest-sub-array boundaries "to print the path(the actual elements)"
        best_left=0
        best_right=0
        for right in range(len(data)):
            current_sum+=data[right]
            while current_sum>s:
                current_sum-=data[left]
                left+=1

            current_len=right-left+1
            if current_len>=max_len:
                max_len=current_len
                best_left=left
                best_right=right

                    
        
           
        print(f"{data[best_left:best_right+1]}")
        print(max_len)

if __name__=="__main__":
    s=Sol()
    data=[1,2,3,4,5,6,7,8,9]
    t=9
    s.longesSubarray(data=data,s=t)


        
    
            

