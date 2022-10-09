class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        visited_set = set()
        nums = sorted(nums)
        results = []
        
        for i in range(len(nums)):
            if (nums[i] not in visited_set):
                self.twoSum(nums, i, results)
                visited_set.add(nums[i])
        
        return results
    
                
    def twoSum(self, nums, index, results):
        start = index+1
        if (start<len(nums) and start+1<len(nums)):
            #print("Here")
            visited_set2 = set()
            end = len(nums)-1
            target = 0-nums[index]
            
            while (start<end):
                #[-4, -1, -1, 0, 1, 2,]
                #print("Here3", start, end)
                #print("...", nums[start], nums[end])
                #print("In the while loop:", nums[start], nums[end])
                val = nums[start]+nums[end]
                if (val == target):
                        #print(start, end)
                        if (nums[start] not in visited_set2):
                            results.append([nums[index], nums[start], nums[end]])
                        #print(start, end)
                            visited_set2.add(nums[start])
                        start +=1
                        end   -=1
                        #print(start, end)
                        
                elif (val > target):
                        #print(start, end)
                        end -=1
                else:
                        #print("else",start, end)
                        start +=1
                
        
                
        
        
        
        
