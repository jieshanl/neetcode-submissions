class MedianFinder:

    def __init__(self):
        # Use two heaps, max heap for lower half, min heap for upper half
        # [1, 2, 3, 4, 5, 6] len(nums) is even
        self.lower = [] # max heap
        self.upper = [] # min heap

    def addNum(self, num: int) -> None: # O(log n)
        # lower: [1, 5], upper: [2, 3, 4]

        # condition: check where num should go to maintain sorted order
        if self.upper and num > self.upper[0]: # if upper is non-empty and num is greater than min in upper
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -1 * num)

        # conditions: if the length of two heaps are roughly equal
        if len(self.lower) > len(self.upper) + 1:
            val = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)
        if len(self.upper) > len(self.lower) + 1:
            val = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -1 * val)
    

    def findMedian(self) -> float: # O(1)
        # when length is odd
        # lower: [1, 2, 3] upper: [4, 5]
        if len(self.lower) > len(self.upper):
            return -1 * self.lower[0]
        elif len(self.upper) > len(self.lower):
            return self.upper[0]
        # else: length is even
        return (-1 * self.lower[0] + self.upper[0]) / 2
        

        
        

        
        