class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        remIdx = {0 : -1}
        remTot = 0
        tot = 0
        # print(remIdx,nums)
        for idx,num in enumerate(nums):
            # print(remTot)
            tot += num
            rem = tot % k
            # print("REM",rem,k,num,remTot)
            
            if rem in remIdx:
                if idx - remIdx[rem] >= 2:
                    return True
            else:
                remIdx[rem] = idx
        # print(remIdx)
        return False