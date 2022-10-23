class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        results = [0]*len(nums)
        start   = 0
        end     = len(nums)-1
        index   = -1
        
        while (start<= end):
            
            if (nums[end]*nums[end] > nums[start]*nums[start]):
                results[index]=(nums[end]*nums[end])
                end -=1
                
            else:
                results[index]=(nums[start]*nums[start])
                start +=1
                
            index -=1
            
        return results
                
        
