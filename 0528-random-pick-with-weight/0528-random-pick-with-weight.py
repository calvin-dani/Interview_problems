class Solution:

    def __init__(self, w: List[int]):
        total = 0        
        self.w = []
        for wgt in w:
            total += wgt
            self.w.append(total)
        self.total = total

    def pickIndex(self) -> int:
        x  = random.randint(1,self.total)
        index = bisect_left(self.w, x)
        # Return the index corresponding to the random number
        return index



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()