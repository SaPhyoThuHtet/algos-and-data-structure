class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
           
        ans = []
        nums = sorted(nums)
        
        for i4 in range(0, len(nums)-3):
            target3 = target-nums[i4]
            self.threeSum(nums,i4, target3, ans)
            
        return ans
            
    def threeSum(self, nums, i4, target3, ans):
        
        for i3 in range(i4+1, len(nums)):
            target2 = target3-nums[i3]
            self.twoSum(nums, i3, i4, target2, ans)
                
                
    def twoSum(self, nums, i3, i4, target2, ans):
        
        start = i3+1
        end = len(nums)-1
        
        while (start<end):
            val = nums[start]+nums[end] 
            if (val== target2):
                result = [nums[i4], nums[i3],nums[start],nums[end]]
                if (result not in ans):
                    ans.append(result)
                start +=1
                end -=1
                
            elif (val<target2):
                start += 1
                
            else:
                end -=1
                
    
        
        
        
            
    
        
