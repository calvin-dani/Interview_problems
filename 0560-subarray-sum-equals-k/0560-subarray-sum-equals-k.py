class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        prefixMap = {0:1}
        tempSum = 0
        
        for idx,num in enumerate(nums):
            tempSum += num
            if (tempSum - k) in prefixMap:
                count += prefixMap[(tempSum - k)]
            
            if tempSum in prefixMap:
                prefixMap[tempSum] += 1
            else:
                prefixMap[tempSum] = 1
                
            
        return count