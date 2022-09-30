class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        #1 2 3
        
        index = 0
        
        for i in nums:
            if (i != val):
                nums[index] = i
                index += 1
        #print(nums)
       # print(index)
        return index
                
                
                
                
            
        
