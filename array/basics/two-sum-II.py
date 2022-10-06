class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        first = 0
        second    = len(numbers)-1
        
        while (first<second):
            
            val = numbers[first]+numbers[second]
            
            if (val == target):
                return [first+1, second+1]
            
            elif (val>target):
                second = second-1
            
            else:
                first = first+1
            
            
        
