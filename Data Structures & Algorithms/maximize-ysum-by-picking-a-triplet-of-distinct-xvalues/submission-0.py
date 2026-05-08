class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        # Use the Hash Map + Min-Heap data structures
        # HashMap: map the x[i] to y[i]

        mp = {}
        for xi, yi in zip(x, y): # [1, 2, 1, 3, 2, 5, 3, 4, 6, 2]
            mp[xi] = max(mp.get(xi, 0), yi)
        
        # now building out minHeap to store the mp.values()
        minHeap = []
        for val in mp.values():
            heapq.heappush(minHeap, val)
            # check if length of minHeap is greater than 3
            if len(minHeap) > 3:
                heapq.heappop(minHeap)
        
        return -1 if len(minHeap) < 3 else sum(minHeap)
