class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        def traversal(cards):

            numDicDis = {}
            minDis = float('inf')
            for idx,num in enumerate(cards):

                if num not in numDicDis:
                    numDicDis[num] = [idx,float('inf')]
                else:
                    oldDis = numDicDis[num][1]
                    newDis = idx - numDicDis[num][0]
                    tempMinDis = min(oldDis,newDis)
                    minDis = min(minDis,tempMinDis)
                    numDicDis[num] = [idx,tempMinDis]
            
            return minDis + 1
        
        

        return traversal(cards) if len(cards) != len(set(cards)) else -1
            