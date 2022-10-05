class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dic = {}
        
        for i in range(len(nums)):
            if (nums[i] in dic and abs(i-dic[nums[i]]) <=k):
                    return True
            dic[nums[i]] = i
        return False
        
