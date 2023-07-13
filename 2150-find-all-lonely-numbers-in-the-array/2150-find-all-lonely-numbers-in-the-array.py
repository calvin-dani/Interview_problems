from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        numCounter = Counter(nums)
        ans = []
        for num in nums:
            if numCounter[num] == 1 and num-1 not in numCounter and num+1 not in numCounter:
                ans.append(num)
        
        return ans