class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python does NOT have maxHeap, so we multiply every stone by -1 and use minHeap
        stones = [-s for s in stones]
        heapq.heapify(stones) # turn this stones into a Heap

        while len(stones) > 1: # if we have 1 stone, we stop the stimulation
            first = heapq.heappop(stones) # pop from maxheap
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

            