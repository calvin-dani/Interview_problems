class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        tempCap = capacity
        idx = -1
        walk = 0
        while idx < len(plants)-1:

            if plants[idx+1] <= tempCap:
                tempCap -= plants[idx+1]
                walk += 1
                idx += 1
            elif plants[idx+1] > tempCap and plants[idx+1] <= capacity:
                tempCap = capacity
                walk += 2 * (idx+1)
           
            print(idx,tempCap,walk)
    
        return walk