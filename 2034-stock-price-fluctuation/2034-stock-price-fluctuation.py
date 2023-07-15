class StockPrice:

    stockTimeStampPrice = {}
    currentTimeStamp = -1
    

    def __init__(self):
        self.stockTimeStampPrice = {}
        self.currentTimeStamp = -1
        self.maxheap = []
        self.minheap = []
        

    def update(self, timestamp: int, price: int) -> None:
        self.currentTimeStamp = max(self.currentTimeStamp,timestamp)
        self.stockTimeStampPrice[timestamp] = price
        heapq.heappush(self.maxheap,(-price,timestamp))
        heapq.heappush(self.minheap,(price,timestamp))
        
    def current(self) -> int:
        return self.stockTimeStampPrice[self.currentTimeStamp] if self.currentTimeStamp in self.stockTimeStampPrice else -1
        
    def maximum(self) -> int:
        price,timestamp = heapq.heappop(self.maxheap)        

        while -price != self.stockTimeStampPrice[timestamp]:
            price,timestamp = heapq.heappop(self.maxheap)

        heapq.heappush(self.maxheap,(price,timestamp))

        return -price

    def minimum(self) -> int:
        price,timestamp = heapq.heappop(self.minheap)        

        while price != self.stockTimeStampPrice[timestamp]:
            price,timestamp = heapq.heappop(self.minheap)

        heapq.heappush(self.minheap,(price,timestamp))
        
        return price

        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()