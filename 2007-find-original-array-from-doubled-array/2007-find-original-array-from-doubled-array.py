from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) < 2 or len(changed) % 2 != 0:
            return []

        letFreq = Counter(changed)
        changed.sort()
        res = []
        resSet = set()
        for num in changed:
            if num == 0 and letFreq[num] >= 2:
                res.append(num)
                letFreq[num] -= 2
            elif letFreq[num] >= 1 and letFreq[num * 2] >= 1 and num > 0:
                res.append(num)
                letFreq[num] -= 1
                letFreq[num * 2] -= 1
            
        return res if len(res) == len(changed)//2 else []