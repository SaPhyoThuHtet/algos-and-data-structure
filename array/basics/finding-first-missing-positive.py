class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        index = 0
        for i in range(len(nums)):
            if (nums[i] >0):
                nums[index] = nums[i]
                index +=1
         
        for i in range(0, index):
            index_to_replace = abs(nums[i])-1
            if (index_to_replace<index and nums[index_to_replace] >0):
                nums[index_to_replace] *= -1
                
        for i in range(0,index):
            if not(nums[i] <0):
                return i+1
        
        return index+1
                
                
        
