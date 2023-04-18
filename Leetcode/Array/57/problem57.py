def insert(self, intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    finalInt = []

    for idx,interval in enumerate(intervals):
        if newInterval[0] > interval[1]:
            finalInt.append(interval)
        elif newInterval[1] < interval[0]:
            finalInt.append(newInterval)
            finalInt.extend(interval[idx:])
            return finalInt
        else:
            newInterval = [
                min([newInterval[0], interval[0]]),
                max([newInterval[1], interval[1]]),
            ]
    
        finalInt.append(newInterval)

    return finalInt
