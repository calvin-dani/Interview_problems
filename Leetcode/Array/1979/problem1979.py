def findGCD(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    minNum = min(nums)
    maxNum = max(nums)
    
    for i in range(minNum,0,-1):
        if minNum % i == 0 and maxNum % i == 0:
            return i

def findGCD2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    minNum = min(nums)
    maxNum = max(nums)
    
    return gcd(minNum,maxNum)

def gcd(minN,maxN):
    if(minN > maxN):
        gcd(maxN,minN)
    if minN == 0:
        return maxN
    return gcd(maxN%minN,minN)
    
print(findGCD([2,5,6,9,10]))