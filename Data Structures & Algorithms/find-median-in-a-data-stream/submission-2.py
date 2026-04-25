class MedianFinder:

    def __init__(self):
        # we will use two heaps, lower half with max heap and upper half with min heap
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        # adding and removing from heaps are O(log n) time
        # [1, 2], [3, 4], the length of both heaps has to be roughly equal
        # the values in lower heap has to be smaller than the upper heap
        # when both heaps are empty, we casually insert num to lower
        heapq.heappush(self.lower, -1 * num) # * -1 because we want max heap for lower

        if (self.lower and self.upper 
            and (-1 * self.lower[0]) > self.upper[0]):
            val = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)

        # check if the length of both heaps are not equal
        if len(self.lower) > len(self.upper) + 1: # if the differnece between the length are more than 2
            val = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)
        if len(self.upper) > len(self.lower) + 1:
            val = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -1 * val)

    def findMedian(self) -> float:
        # when the length are odds
        if len(self.lower) > len(self.upper): # [1, 2, 3], [4, 5]
            return -1 * self.lower[0]
        if len(self.upper) > len(self.lower): # [1, 2], [3, 4, 5]
            return self.upper[0]
        # else case: length of both heaps are equal, we have even length
        return (-1 * self.lower[0] + self.upper[0]) / 2

        
        

        
        