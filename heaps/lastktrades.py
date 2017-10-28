import heapq
class LastKStocks: 
    def __init__(self, k):
        self._k = k 
        self._counter = 1
        self._min_heap = []
        self._size = 0        
        heapq.heapify(self._min_heap)
    
    def add_trade(self, symbol):        
        if self._size < self._k:
            heapq.heappush(self._min_heap, (self._counter, symbol)) 
            self._size += 1    
        else: 
            heapq.heappushpop(self._min_heap, (self._counter, symbol))
        
        self._counter += 1
    
    def get_trades(self):
        return [p[1] for p in heapq.nlargest(self._k, self._min_heap)]
    
if __name__ == '__main__':
    s = LastKStocks(2)
    s.add_trade("IBM")
    s.add_trade("USB")
    s.add_trade("RAR")
    print(s.get_trades())