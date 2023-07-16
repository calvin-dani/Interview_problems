class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        res = []
        for time in timePoints:
            hrmin = time.split(":")
            hour = int(hrmin[0])
            miniute = int(hrmin[1]) 
            res.append((hour * 60) + miniute)
        
        res.sort()
        res.append(res[0]+(60*24))
        minRes = float('inf')
        prevTime = 0
        for idx,time in enumerate(res):
            if idx == 0:
                prevTime = time
                continue
            
            minRes = min(minRes,time-prevTime)
            prevTime = time
            
        return minRes