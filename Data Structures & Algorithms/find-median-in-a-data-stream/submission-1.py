class MedianFinder:

    def __init__(self):
        # two heaps, max heap for lower half, min heap for upper half
        # two heaps should be equal length
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        #consider adding it to two unbalanced heaps 
        heapq.heappush(self.lower, -1 * num) # since Python goes with min heap by default

        # make sure every num in lower half is <= every num in upper half 
        # because we want them to be sorted in ascending order
        if (self.lower and self.upper and 
            (-1 * self.lower[0]) > self.upper[0]):
            val = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)

        # check if length of both heaps are not the same
        if len(self.lower) > len(self.upper) + 1: # if the length difference is 2 or greater
            val = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)
        if len(self.upper) > len(self.lower) + 1: 
            val = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -1 * val)

    def findMedian(self) -> float:
        # check if the length is odd
        if len(self.lower) > len(self.upper): # 3 vs. 2, lower has an extra element
            return -1 * self.lower[0] # return the largest value in lower
        if len(self.upper) > len(self.lower): # an extra value in upper
            return self.upper[0]
        # else we have even length
        return (-1 * self.lower[0] + self.upper[0]) / 2
        

        
        