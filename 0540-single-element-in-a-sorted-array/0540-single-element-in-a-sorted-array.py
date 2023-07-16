class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            
            mid = (low + high) // 2
            
            # print(low,high,mid,nums[mid])
            
            if mid == len(nums) - 1:
                if nums[mid] != nums[mid-1]:
                    return nums[mid]
                else:
                    high = mid
            elif mid == 0:
                if nums[mid] != nums[mid+1]:
                    return nums[mid]
                else:
                    low = mid
            elif nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                    return nums[mid]
            elif mid % 2 == 0:
                if nums[mid] == nums[mid-1]:
                    high = mid
                else:
                    low = mid 
            elif mid % 2 == 1:
                if nums[mid] == nums[mid+1]:
                    high = mid
                else: 
                    low = mid + 1
        
        return nums[low]
            