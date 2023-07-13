class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
       
        if len(nums) == 0:
            return []
        
        maxRes = nums.count(1)
        res = maxRes
        ans = [0]
        for idx,ele in enumerate(nums):
            if ele == 0:
                newRes = res + 1
            else:
                newRes = res - 1
            if newRes > maxRes:
                maxRes = newRes
                ans = [idx+1]
            elif newRes == maxRes:
                ans.append(idx+1)
            res = newRes
            
                    
        return ans
